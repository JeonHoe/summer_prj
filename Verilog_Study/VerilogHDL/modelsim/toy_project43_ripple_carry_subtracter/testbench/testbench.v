`timescale 1ns/1ps
module testbench();
    
    reg [31:0] a, b;
    wire [31:0] res;
    wire c_out;

    ripple_carry_subtract rcs1(res, c_out, a, b);

    initial
    begin
        a = 32'h5555_5555; b = 32'h5555_5555;
        #10 $stop;
    end

endmodule