`timescale 1ns/1ps
module testbench();
    
    reg d_in, ld, clk, reset;
    reg [3:0] pd_in;
    wire out;

    register_diff2 rd1(out, pd_in, d_in, ld, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0; ld = 1'b0; d_in = 1'b0; pd_in = 4'b0101;
        #10 reset = ~reset;
        #20 ld = ~ld; d_in = 1'b1;
        #10 ld = ~ld;
        #10 d_in = 1'b0;
        #90 $stop;
    end

endmodule