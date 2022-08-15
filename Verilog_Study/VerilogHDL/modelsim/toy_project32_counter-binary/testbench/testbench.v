`timescale 1ns/1ps
module testbench();
    
    reg clk, reset, ud;
    wire [3:0] out;

    binary_counter bc1(out, clk, reset, ud);

    initial clk = 1'b1;

    initial
    begin
        ud = 1'b0;
        #70 ud = ~ud;
    end

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b1;
        #10 reset = ~reset;
        #110 $stop;
    end

endmodule