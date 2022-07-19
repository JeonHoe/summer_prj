module decoder(in, out1, out2, out3, out4, out5, out6, out7, out8);

    input [2:0] in;
    output out1, out2, out3, out4, out5, out6, out7, out8;

    assign out1 = ~in[2] && ~in[1] && ~in[0];
    assign out2 = ~in[2] && ~in[1] && in[0];
    assign out3 = ~in[2] && in[1] && ~in[0];
    assign out4 = ~in[2] && in[1] && in[0];
    assign out5 = in[2] && ~in[1] && ~in[0];
    assign out6 = in[2] && ~in[1] && in[0];
    assign out7 = in[2] && in[1] && ~in[0];
    assign out8 = in[2] && in[1] && in[0];

endmodule