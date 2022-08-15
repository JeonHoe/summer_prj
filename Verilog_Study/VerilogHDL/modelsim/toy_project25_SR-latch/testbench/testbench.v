`timescale 1ns/1ps
module testbench();
    
    reg s, r, reset;
    wire q, q_bar;

    SR_latch sr1(q, q_bar, s, r, reset);

    initial
    begin
        reset = 1'b1;
        #10 reset = ~reset;
    end

    initial
    begin
        s <= 1'b0; r <= 1'b0;
        #20 s <= 1'b1; r <= 1'b0;
        #10 s <= 1'b0; r <= 1'b0;
        #10 s <= 1'b0; r <= 1'b1;
        #10 s <= 1'b0; r <= 1'b0;
        #10 $stop;
    end

endmodule