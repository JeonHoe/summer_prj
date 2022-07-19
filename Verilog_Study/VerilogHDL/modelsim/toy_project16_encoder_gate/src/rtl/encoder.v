module encoder(out, in1, in2, in3, in4, in5, in6, in7, in8);

    input in1, in2, in3, in4, in5, in6, in7, in8;
    output [2:0] out;

    assign out = (in1 == 1'b1) ? 3'h0 :
                 (in2 == 1'b1) ? 3'h1 :
                 (in3 == 1'b1) ? 3'h2 :
                 (in4 == 1'b1) ? 3'h3 :
                 (in5 == 1'b1) ? 3'h4 :
                 (in6 == 1'b1) ? 3'h5 :
                 (in7 == 1'b1) ? 3'h6 :
                 (in8 == 1'b1) ? 3'h7 : 3'hz;

endmodule