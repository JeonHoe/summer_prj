`timescale 1ns/1ps
module testbench();
    
    reg d, clk, reset;
    wire q, qb;

    D_ff dff1(q, qb, d, clk, reset);

    initial clk = 1'b0;

    always #5 clk = ~clk;

    initial
    begin
        reset = 1'b1;
        #12 reset = ~reset;
        #65 reset = ~reset;
        #8 reset = ~reset;
    end

    initial
    begin
        d = 1'b1;
        #17 d = 1'b0;
        #15 d = 1'b1;
        #20 d = 1'b0;
        #20 d = 1'b1;
        #20 $stop;
    end

endmodule