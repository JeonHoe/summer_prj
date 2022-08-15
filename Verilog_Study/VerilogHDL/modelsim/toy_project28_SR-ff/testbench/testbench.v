`timescale 1ns/1ps
module testbench();
    
    reg s, r, clk, reset;
    wire q, qb;

    SR_ff srff1(q, qb, s, r, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b1;
        #10 reset = ~reset;
    end

    initial
    begin
        s <= 1'b0; r <= 1'b0;
        #30 s <= 1'b1; r <= 1'b0;
        #20 s <= 1'b0; r <= 1'b0;
        #20 s <= 1'b0; r <= 1'b1;
        #20 s <= 1'b0; r <= 1'b0;
        #30 $stop;
    end

endmodule