`timescale 1ns/1ps
module testbench();
    
    reg clk, rst_n;
    wire in0, in1, in2, out;

    quiz02_diff qd2 (clk, rst_n, in0, in1, in2);
    input3_and a1 (in0, in1, in2, out);

    initial clk = 1'b0;

    always #5 clk = ~clk;

    initial
    begin
        rst_n = 1'b0;
        #2 rst_n = ~rst_n;
        #245 $stop;
    end

endmodule