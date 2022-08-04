`timescale 1ns/1ps
module testbench();
    
    reg [3:0] M, Q;
    wire [7:0] product;

    booth_multiplier bm1 (product, M, Q);


    initial
    begin
        M = 4'b0110; Q = 4'b1011;
        #100 $stop;
    end

endmodule