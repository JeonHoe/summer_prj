`timescale 1ns/1ps
module test(clk, a, b, c, out);

    input clk, a, b;
    input [2:0]c;
    output out;

    assign out = c + (a && b);

endmodule