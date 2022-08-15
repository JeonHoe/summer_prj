`timescale 1ns/1ps
module testbench();
    
    reg ld, clk, reset;
    reg [3:0] d_in;
    wire out;

    register r1(out, d_in, ld, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        ld = 1'b0; reset = 1'b0; d_in = 4'b0101;
        #10 reset = ~reset;
        #20 ld = ~ld;
        #10 ld = ~ld;
        #100 $stop;
    end

endmodule