`timescale 1ns/1ps
module testbench();
    
    reg d_in, clk, reset;
    wire [3:0] out;

    register_diff rd1(out, d_in, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0; d_in = 1'b0;
        #10 reset = ~reset;
        #20 d_in = 1'b1;
        #20 d_in = 1'b0;
        #20 d_in = 1'b1;
        #20 d_in = 1'b1;
        #50 $stop;
    end

endmodule