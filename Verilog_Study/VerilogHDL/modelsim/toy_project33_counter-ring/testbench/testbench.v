`timescale 1ns/1ps
module testbench();
    
    reg clk, reset;
    wire [2:0] out;

    ring_counter rc1(out, clk, reset);

    initial clk = 1'b0;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0;
        #15 reset = ~reset;
        #50 reset = ~reset;
        #10 reset = ~reset;
        #140 $stop;
    end

endmodule