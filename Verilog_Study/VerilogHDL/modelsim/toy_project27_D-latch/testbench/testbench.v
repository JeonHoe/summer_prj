`timescale 1ns/1ps
module testbench();
    
    reg d, reset;
    wire q, qb;

    D_latch d1(q, qb, d, reset);

    initial
    begin
        reset = 1'b1;
        #10 reset = ~reset;
    end

    initial
    begin
        d = 1'b0;
        #20 d = 1'b1; 
        #10 d = 1'b0;
        #10 $stop;
    end

endmodule