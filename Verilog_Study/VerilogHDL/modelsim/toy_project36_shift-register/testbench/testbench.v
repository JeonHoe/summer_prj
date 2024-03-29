`timescale 1ns/1ps
module testbench();
    
    reg clk, ld, sl, sr, reset;
    reg [3:0] d_in;
    wire [3:0] out;

    shift_register shftreg1(out, d_in, clk, ld, sl, sr, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b0; ld = 1'b0; sl = 1'b0; sr = 1'b0; d_in = 4'b1011;
        #10 reset = ~reset;
        #20 ld = ~ld;
        #10 ld = ~ld;
        #30 sl = ~sl;
        #10 sl = ~sl;
        #30 sr = ~sr;
        #10 sr = ~sr;
        #60 $stop;
    end

endmodule