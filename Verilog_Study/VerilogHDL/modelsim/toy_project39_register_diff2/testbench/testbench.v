`timescale 1ns/1ps
module testbench();
    
    reg d_in, ld, clk, reset;
    reg [3:0] pd_in;
    wire out;

    register_diff2 rd1(out, pd_in, d_in, ld, clk, reset);

    initial clk = 1'b0;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0; ld = 1'b0; d_in = 1'b1; pd_in = 4'b1011;
        #15 reset = ~reset;
        #10 ld = ~ld;
        #10 ld = ~ld; d_in = 1'b0;
        #20 d_in = 1'b1;
        #20 d_in = 1'b0;
        #20 d_in = 1'b1;
        #80 $stop;
    end

endmodule