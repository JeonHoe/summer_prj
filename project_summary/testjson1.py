#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import itertools
import json5
import jsonschema
import time
import traceback
import sys

__doc__ = """
asciiwave is a tool to convert WaveDrom timing diagrams into ASCII art.

For example:

```
$ cat example/step3.json
{ signal: [
  { name: "clk",  wave: "P......" },
  { name: "bus",  wave: "x.==.=x", data: ["head", "body", "tail", "data"] },
  { name: "wire", wave: "0.1..0." }
]}

$ ./asciiwave example/step3.json
      ┏──┐  ┏──┐  ┏──┐  ┏──┐  ┏──┐  ┏──┐  ┏──┐  
clk : ┛  └──┛  └──┛  └──┛  └──┛  └──┛  └──┛  └──
      xxxxxxxxxxxx╱    ╲╱          ╲╱    ╲xxxxxx
bus : xxxxxxxxxxxx╲head╱╲   body   ╱╲tail╱xxxxxx
      ┐           ┌─────────────────┐           
wire: └───────────┘                 └───────────
```

It supports:
- `wave` commands: `1hHu 0lLd pPnN =2345 zx |`
- The `data` signal property: either an array of strings, or a single string
  containing whitespace-separated values.
- The `hscale` config property: the width of each time unit is `hscale * 2 + 2`
  characters.
- The `period` signal property: this can be a floating point number. The width
  of each wave unit, in characters, is multiplied by `period` and rounded down.
- The `phase` signal property: this can be a floating point number. The signal
  is advanced (if positive) or retarded (negative) by this number of periods.

Watch mode (-w) will continously poll a file on disk, and redraw whenever the
file changes. This can be used interactively alongside a text editor.

"""

# First the key, then the graphics lines
graphics_tiny = [
	"0+1-rfxz< >|UuDd",
	"_┌─┐┏┓xz< >┆╭┄╰┄",
]

graphics_default = [
	"0+1-rfxz< >|UuDd",
	" ┌─┐┏┓x_╱ ╲┆╭┄  ",
	"─┘ └┛┗x ╲ ╱┆  ╰┄"
]

graphics_tall = [
	"0+1-rfxz< >|UuDd",
	" ┌─┐┏┓x ╱ ╲┆╭┄  ",
	" │ │┃┃x─   ┆┆ ┆ ",
	"─┘ └┛┗x ╲ ╱┆  ╰┄"
]

# Define the WaveJSON subset we support
wavejson_schema = {
	"type": "object",
	"properties": {
		"config": {
			"type": "object",
			"properties": {
				"hscale": {"type": "number"}
			}
		},
		"signal": {
			"type": "array",
			"items": [
				{
					"type": "array",
					"items": [
						{
						"type": "string"
						},
						{
							"type": "object",
							"properties": {
								"name": {"type": "string"},
								"wave": {"type": "string"},
								"data": {
									"type": ["array", "string"],
									"items": {"type": "string"}
								},
								"phases": {"type": "number"},
								"period": {"type": "number"}
							}
						}
					]
				},
				{
					"type": "object",
					"properties": {
						"name": {"type": "string"},
						"wave": {"type": "string"},
						"data": {
							"type": ["array", "string"],
							"items": {"type": "string"}
						},
						"phases": {"type": "number"},
						"period": {"type": "number"}
					}
				}
			]
		}
	}
}

# WaveDrom behaviour is surprisingly complex; this is an approximation
def cmd_10(cmd, prev_cmd, width, charwidth, data, put):
	h_cmds = "1hHu"
	l_cmds = "0lLd"
	high = cmd in h_cmds
	hard_edge = cmd in "HL" or \
		(high and prev_cmd in (l_cmds + "zx=2345")) or \
		(not high and prev_cmd in (h_cmds + "zx=2345")) or \
		(cmd in "1h" and prev_cmd in "1pP") or \
		(cmd in "0l" and prev_cmd in "0nN")
	if cmd == "u":
		edge, flat = ("U", "u")
	elif cmd == "d":
		edge, flat = ("D", "d")
	elif cmd == "H":
		edge, flat = ("r", "1")
	elif cmd == "L":
		edge, flat = ("f", "0")
	elif high:
		edge, flat = ("+", "1")
	else:
		edge, flat = ("-", "0")
	rendered = edge * hard_edge + flat * (width - hard_edge)
	for s in rendered:
		put(s)

def cmd_clk(cmd, prev_cmd, width, charwidth, data, put):
	shape = {
		"p": "+1-0",
		"P": "r1-0",
		"n": "-0+1",
		"N": "f0+1"
	}[cmd]
	if (cmd == "p" and prev_cmd in "hH") or (cmd == "n" and prev_cmd in "lL"):
		shape = shape[1] + shape[1:]
	for i in range(width // charwidth):
		put(shape[0])
		for j in range(charwidth // 2 - 1):
			put(shape[1])
		put(shape[2])
		for j in range(charwidth // 2 - 1):
			put(shape[3])

def cmd_bus(cmd, prev_cmd, width, charwidth, data, put):
	assert(cmd in "=2345")
	if len(data) > 0:
		contents = data.pop(0)
	else:
		contents = ""
	space = width - 2
	contents = contents[:min(len(contents), space)]
	contents = "{: ^{}}".format(contents, space)
	put("<")
	for c in contents:
		put(c, raw_char=True)
		# for i in range(len(outs)):
		# 	outs[i] += c if i == len(outs) // 2 else " "
	put(">")

def cmd_separator(cmd, prev_cmd, width, charwidth, data, put):
	put("|")


def cmd_other(cmd, prev_cmd, width, charwidth, data, put):
	for i in range(width):
		put(cmd.lower())

# Create callback for appending some wave state's graphics to an array of strings
def create_put(outs, graphics_map):
	def put(c, raw_char=False):
		for i in range(len(outs)):
			if raw_char:
				outs[i] += c if i == len(outs) // 2 else " "
			else:
				outs[i] += graphics_map[c][i]
	return put

def render_signal(wave, data, charwidth, graphics_map):
	if not hasattr(render_signal, "handlers"):
		render_signal.handlers = {}
		for c in "1hHu0lLd":
			render_signal.handlers[c] = cmd_10
		for c in "pPnN":
			render_signal.handlers[c] = cmd_clk
		for c in "=2345":
			render_signal.handlers[c] = cmd_bus
		for c in "xXzZ":
			render_signal.handlers[c] = cmd_other
		render_signal.handlers["|"] = cmd_separator
	assert(charwidth >=4 and charwidth % 2 == 0)

	outs = [""] * len(graphics_map[" "])
	put = create_put(outs, graphics_map)
	if type(data) is str:
		data = data.split()
	else:
		data = data[:]
	prev_cmd = "x"
	wstream = iter(wave)

	while True:
		cmd = next(wstream, None)
		if cmd is None:
			break
		if cmd == ".":
			cmd = prev_cmd
		if cmd not in render_signal.handlers:
			cmd = "x"
		width = charwidth
		# . refers to command *before* |, so terminate early and don't touch prev_cmd
		while cmd != "|":
			next_cmd = next(wstream, None)
			if next_cmd == ".":
				width += charwidth
			else:
				wstream = itertools.chain([next_cmd], wstream)
				break
		render_signal.handlers[cmd](cmd, prev_cmd, width, charwidth, data, put)
		if cmd != "|":
			prev_cmd = cmd

	return outs

def render_json(src, out, graphics, force_hscale=None):
	# Currently we spend ~95% of our time in the JSON parser
	obj = json5.loads(src)
	jsonschema.Draft6Validator(wavejson_schema).validate(obj)
	graphics_map = dict(zip(graphics[0], zip(*graphics[1:])))
	# Find longest signal name, and handle config
	max_name_len = 0
	for s in obj["signal"]:
		if type(s) is list:
			for p in s:
				if "name" in p:
					max_name_len = max(max_name_len, len(p["name"]))
		elif "name" in s:
			max_name_len = max(max_name_len, len(s["name"]))
	try:
		hscale = int(obj["config"]["hscale"] * 2 + 2)
	except KeyError:
		hscale = 6
	if force_hscale is not None:
		hscale = force_hscale * 2 + 2

	# Second pass: actually render
	for s in (obj["signal"] if "signal" in obj else []):
		if len(s) == 0:
			print("")
			continue
		if type(s) is list:
			print(s[0])
			for k in range(1, len(s)):
				name = s[k]["name"] if "name" in s[k] else ""
				name_just = "{: <{}}: ".format(name, max_name_len)
				charwidth = int(s[k]["period"] * hscale) if "period" in s[k] else hscale
				lead = int(s[k]["phase"] * charwidth) if "phase" in s[k] else 0
				lag = max(-lead, 0)
				lead = max(lead, 0)
				sig_lines = render_signal(
					s[k]["wave"] if "wave" in s[k] else "",
					s[k]["data"] if "data" in s[k] else [], charwidth, graphics_map)
				for i, l in enumerate(sig_lines):
					if i == len(graphics_map[" "]) - 1:
						out.write(name_just)
					else:
						out.write(" " * len(name_just))
					out.write(" " * lag)
					out.write(l[lead:] + "\n")
		else:
			name = s["name"] if "name" in s else ""
			name_just = "{: <{}}: ".format(name, max_name_len)
			charwidth = int(s["period"] * hscale) if "period" in s else hscale
			lead = int(s["phase"] * charwidth) if "phase" in s else 0
			lag = max(-lead, 0)
			lead = max(lead, 0)
			sig_lines = render_signal(
				s["wave"] if "wave" in s else "",
				s["data"] if "data" in s else [], charwidth, graphics_map)
			for i, l in enumerate(sig_lines):
				if i == len(graphics_map[" "]) - 1:
					out.write(name_just)
				else:
					out.write(" " * len(name_just))
				out.write(" " * lag)
				out.write(l[lead:] + "\n")

def posint(x):
	_x = int(x)
	if _x <= 0:
		raise TypeError(x)
	return _x

if __name__ == "__main__":
	# Preserve newlines in docstring:
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.epilog = __doc__
	parser.add_argument("src", help="WaveJSON source file")
	parser.add_argument("-w", "--watch", action="store_true",
		help="Watch file, continuously update and redraw")
	parser.add_argument("-g", "--graphics", choices=["default", "tiny", "tall"],
		default="default", help="Use a different graphics tileset")
	parser.add_argument("--hscale", type=posint,
		help="Force hscale to a different value than specified in src config.")
	args = parser.parse_args()

	graphics = {
		"default": graphics_default,
		"tiny": graphics_tiny,
		"tall": graphics_tall
	}[args.graphics]

	if args.watch:
		prev_src = None
		while True:
			ifile = open(args.src)
			src = ifile.read()
			ifile.close()
			if src != prev_src:
				print("\033[H\033[J") # VT100 clear command
				try:
					render_json(src, sys.stdout, graphics, force_hscale=args.hscale)
				except Exception:
					traceback.print_exc(file=sys.stdout)
				print("\nWatching file " + args.src)
				print("Ctrl-C to exit")
				prev_src = src
			time.sleep(0.2)
	else:
		ifile = open(args.src)
		render_json(ifile.read(), sys.stdout, graphics, force_hscale=args.hscale)