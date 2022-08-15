`timescale 1ns/1ps
module testbench();
    
    reg j, k, clk, reset;
    wire q, qb;

    JK_ff jkff1(q, qb, j, k, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b1;
        #10 reset = ~reset;
    end

    initial
    begin
        j <= 1'b0; k <= 1'b0;
        #30 j <= 1'b1; k <= 1'b0;
        #20 j <= 1'b0; k <= 1'b0;
        #20 j <= 1'b0; k <= 1'b1;
        #20 j <= 1'b0; k <= 1'b0;
        #20 j <= 1'b1; k <= 1'b1;
        #20 j <= 1'b0; k <= 1'b0;
        #30 $stop;
    end

endmodule