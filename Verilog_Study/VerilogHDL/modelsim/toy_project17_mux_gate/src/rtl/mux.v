module mux(out, in1, in2, in3, in4, in5, in6, in7, in8, sel);

    input [3:0] in1, in2, in3, in4, in5, in6, in7, in8;
    input [2:0] sel;
    output [3:0] out;

    assign out = (sel == 3'b000) ? in1 :
                 (sel == 3'b001) ? in2 :
                 (sel == 3'b010) ? in3 :
                 (sel == 3'b011) ? in4 :
                 (sel == 3'b100) ? in5 :
                 (sel == 3'b101) ? in6 :
                 (sel == 3'b110) ? in7 :
                 (sel == 3'b111) ? in8 : 4'bx;

endmodule