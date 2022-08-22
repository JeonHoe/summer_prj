import json


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
				{"type": "array",
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
					}, "additionalProperties": False
				}]},
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
					}, "additionalProperties": False
				}
			]
		}
	},
	"additionalProperties": False
}

def in_pont(dict1):
	if (type(dict1) is not dict):
		print("Error Datatype;;")
		return (None, None)
	else:
		list_in = []
		for cmd in dict1.values():
				for k in cmd:
					if (type(k) is list):
						if (k[0] == "input"):
							for i in range(1, len(k)):
								list_in.append(k[i]["name"])
					else:
						pass
		return list_in

def wave(dict1):
	if (type(dict1) is not dict):
		print("Error Datatype;;")
		return (None, None)
	else:
		list_wave = []
		for cmd in dict1.values():
				for k in cmd:
					if (type(k) is list):
						if(k[0] == "input"):
							for i in range(1, len(k)):
								list_wave.append(k[i]["wave"])
					else:
						pass
		return list_wave

def data(dict1):
	if (type(dict1) is not dict):
		print("Error Datatype;;")
		return (None, None)
	else:
		list_data = []
		for cmd in dict1.values():
				for k in cmd:
					if (type(k) is list):
						if(k[0] == "input"):
							for i in range(1, len(k)):
								if "data" is not k[i]:
									list_data.append("")
								else:
									list_data.append(k[i]["data"])
					else:
						pass
		return list_data


def make_reg(l_in):
	for s in l_in:
		print(reg)



def call_json(str):
	with open(str, "r") as fp:
		res = json.load(fp)
	return res

str = "test.json"

dict1 = call_json(str)
    
reg = in_pont(dict1)

print(reg)

wave1 = wave(dict1)

print(wave1)

data1 = data(dict1)

print(data1)
