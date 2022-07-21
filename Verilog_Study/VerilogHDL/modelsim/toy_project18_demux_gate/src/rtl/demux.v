module demux(in, sel, out1, out2, out3, out4, out5, out6, out7, out8);

    input [3:0] in;
    input [2:0] sel;
    output [3:0] out1, out2, out3, out4, out5, out6, out7, out8;

    assign out1 = (sel == 3'b000) ? in : 4'b0;
    assign out2 = (sel == 3'b001) ? in : 4'b0;
    assign out3 = (sel == 3'b010) ? in : 4'b0;
    assign out4 = (sel == 3'b011) ? in : 4'b0;
    assign out5 = (sel == 3'b100) ? in : 4'b0;
    assign out6 = (sel == 3'b101) ? in : 4'b0;
    assign out7 = (sel == 3'b110) ? in : 4'b0;
    assign out8 = (sel == 3'b111) ? in : 4'b0;

endmodule