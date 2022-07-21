`timescale 1ns/1ps
module testbench();
    
    reg s, r, clk, reset;
    wire q, qb;

    SR_ff srff1(q, qb, s, r, clk, reset);

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
        s <= 1'b1; r <= 1'b0;
        #18 s <= 1'b0; r <= 1'b0;
        #20 s <= 1'b0; r <= 1'b1;
        #10 s <= 1'b0; r <= 1'b0;
        #25 s <= 1'b1; r <= 1'b0;
        #30 s <= 1'b0; r <= 1'b1;
        #10 s <= 1'b0; r <= 1'b0;
        #20 $stop;
    end

endmodule