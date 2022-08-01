`timescale 1ns/1ps
module testbench();
    
    reg [31:0] a, b;
    reg  sel;
    wire [31:0] sum;
    wire c_out;

    bit32_CLAS cla1(sum, c_out, a, b, sel);

    initial
    begin
        a = 32'h5555_5555; b = 32'haaaa_aaaa; sel = 1'b1;
        #10 $stop;
    end

endmodule