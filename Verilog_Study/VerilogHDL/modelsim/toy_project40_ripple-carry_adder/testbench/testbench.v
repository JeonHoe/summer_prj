`timescale 1ns/1ps
module testbench();
    
    reg [31:0] a, b;
    reg  c_in;
    wire [31:0] sum;
    wire c_out;

    ripple_carry_add ra1(sum, c_out, a, b, c_in);

    initial
    begin
        a = 32'h5555_5555; b = 32'haaaa_aaaa; c_in = 1'b1;
        #10 $stop;
    end

endmodule