`timescale 1ns/1ps
module testbench();
    
    reg [3:0] x, y;
    wire [7:0] product;

    add_shift_multiplier asm (product, x, y);

    initial
    begin
        x = 4'b0011; y = 4'b0011;
        #10 $stop;
    end

endmodule