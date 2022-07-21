`timescale 1ns/1ps
module testbench();
    
    reg j, k, clk, reset;
    wire q, qb;

    JK_ff jkff1(q, qb, j, k, clk, reset);

    initial clk = 1'b0;

    always #5 clk = ~clk;

    initial
    begin
        reset = 1'b1;
        #10 reset = ~reset;
        #72 reset = ~reset;
        #5 reset = ~reset;
    end

    initial
    begin
        j <= 1'b1; k <= 1'b0;
        #17 j <= 1'b0; k <= 1'b0;
        #20 j <= 1'b0; k <= 1'b1;
        #10 j <= 1'b0; k <= 1'b0;
        #25 j <= 1'b1; k <= 1'b0;
        #30 j <= 1'b0; k <= 1'b1;
        #10 j <= 1'b1; k <= 1'b1;
        #10 j <= 1'b0; k <= 1'b0;
        #10 j <= 1'b1; k <= 1'b1;
        #10 j <= 1'b0; k <= 1'b0;
        #20 $stop;
    end

endmodule