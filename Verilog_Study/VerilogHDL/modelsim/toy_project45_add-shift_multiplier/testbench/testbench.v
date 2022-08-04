`timescale 1ns/1ps
module testbench();
    
    reg [3:0] a, b;
    wire [7:0] product;

    bit4_SASM b4sasm1 (product, a, b);

    initial
    begin
        a = 4'b1101; b = 4'b0011;
        #10 $stop;
    end

endmodule