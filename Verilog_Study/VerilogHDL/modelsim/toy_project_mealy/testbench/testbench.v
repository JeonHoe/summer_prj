`timescale 1ns/1ps

module testbench();

    reg clk, reset, din;
    wire dout;

    det_011_mealy d011mealy (clk, reset, din, dout);

    initial clk = 1'b0;

    always #10 clk = ~clk;

    initial
    begin
       reset = 1'b0; din = 1'b0;
       #15 reset = ~reset;
       #45 din = 1'b1;
       #20 din = ~din;
       #20 $stop;
    end

endmodule
