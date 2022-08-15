`timescale 1ns/1ps
module testbench();
    
    reg d, clk, reset;
    wire q, qb;

    D_ff dff1(q, qb, d, clk, reset);

    initial clk = 1'b1;

    always #10 clk = ~clk;

    initial
    begin
        reset = 1'b1;
        #10 reset = ~reset;
    end

    initial
    begin
        d = 1'b0;
        #30 d = 1'b1;
        #20 d = 1'b0;
        #30 $stop;
    end

endmodule