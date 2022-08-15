`timescale 1ns/1ps
module testbench();
    
    reg clk, reset;
    wire [2:0] out;

    gray_counter gc1(out, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0;
        #10 reset = ~reset;
        #170 $stop;
    end

endmodule