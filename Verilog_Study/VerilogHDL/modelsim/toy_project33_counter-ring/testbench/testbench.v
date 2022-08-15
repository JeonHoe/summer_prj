`timescale 1ns/1ps
module testbench();
    
    reg clk, reset;
    wire q1, q2, q3;

    ring_counter rc1(q1, q2, q3, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0;
        #10 reset = ~reset;
        #150 $stop;
    end

endmodule