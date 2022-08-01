`timescale 1ns/1ps
module testbench();
    
    reg [31:0] a, b;
    reg  c_in;
    wire [31:0] sum, c_out;

    bit32_CLA cla1(sum, c_out, a, b, c_in);

    initial
    begin
        a = 32'h5555_5555; b = 32'haaaa_aaaa; c_in = 1'b0;
        #10 $stop;
    end

endmodule