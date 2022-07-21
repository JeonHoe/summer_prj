`timescale 1ns/1ps
module testbench();
    
    reg t, clk, reset;
    wire q, qb;

    T_ff tff1(q, qb, t, clk, reset);

    initial clk = 1'b0;

    always #5 clk = ~clk;

    initial
    begin
        reset = 1'b1;
        #12 reset = ~reset;
        #55 reset = ~reset;
        #10 reset = ~reset;
    end

    initial
    begin
        t = 1'b1;
        #17 t = 1'b0;
        #15 t = 1'b1;
        #20 t = 1'b0;
        #20 t = 1'b1;
        #20 $stop;
    end

endmodule