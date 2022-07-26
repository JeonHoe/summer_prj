`timescale 1ns/1ps
module testbench();
    
    reg clk, reset;
    wire [2:0] out;

    gray_counter gc1(out, clk, reset);

    initial clk = 1'b0;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0;
        #15 reset = ~reset;
        #40 reset = ~reset;
        #10 reset = ~reset;
        #185 $stop;
    end

endmodule