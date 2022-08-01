`timescale 1ns/1ps
module testbench();
    
    reg d_in, clk, reset;
    wire [3:0] out;

    register_diff rd1(out, d_in, clk, , reset);

    initial clk = 1'b0;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0; d_in = 1'b0;
        #15 reset = ~reset;
        #10 d_in = 1'b1;
        #20 d_in = 1'b0;
        #20 d_in = 1'b1;
        #20 d_in = 1'b1;
        #25 $stop;
    end

endmodule