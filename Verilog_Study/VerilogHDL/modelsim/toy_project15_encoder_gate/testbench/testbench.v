module testbench();
    
    reg in1, in2, in3, in4, in5, in6, in7, in8;
    wire [2:0] out;

    encoder ec1 (out, in1, in2, in3, in4, in5, in6, in7, in8);

    initial
    begin
        in1 = 0;
        in2 = 0;
        in3 = 0;
        in4 = 0;
        in5 = 0;
        in6 = 0;
        in7 = 0;
        in8 = 0;
    end

    initial
    begin
        in1 = 1'b0;
        #10 in1 = 1'b1;
        #10; in1 = 1'b0; in2 = 1'b1;
        #10; in2 = 1'b0; in3 = 1'b1;
        #10; in3 = 1'b0; in4 = 1'b1;
        #10; in4 = 1'b0; in5 = 1'b1;
        #10; in5 = 1'b0; in6 = 1'b1;
        #10; in6 = 1'b0; in7 = 1'b1;
        #10; in7 = 1'b0; in8 = 1'b1;
        #10; $stop;
    end

endmodule