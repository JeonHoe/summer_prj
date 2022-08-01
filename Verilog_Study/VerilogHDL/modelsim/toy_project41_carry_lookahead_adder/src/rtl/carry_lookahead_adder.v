module bit32_CLA (sum, c_out, a, b, c_in);

    input [31:0] a, b;
    input c_in;
    output [31:0] sum;
    output c_out;

    wire [6:0] c;

    bit4_CLA b4cla1 (sum[3:0], c[0], a[3:0], b[3:0], c_in);
    bit4_CLA b4cla2 (sum[7:4], c[1], a[7:4], b[7:4], c[0]);
    bit4_CLA b4cla3 (sum[11:8], c[2], a[11:8], b[11:8], c[1]);
    bit4_CLA b4cla4 (sum[15:12], c[3], a[15:12], b[15:12], c[2]);
    bit4_CLA b4cla5 (sum[19:16], c[4], a[19:16], b[19:16], c[3]);
    bit4_CLA b4cla6 (sum[23:20], c[5], a[23:20], b[23:20], c[4]);
    bit4_CLA b4cla7 (sum[27:24], c[6], a[27:24], b[27:24], c[5]);
    bit4_CLA b4cla8 (sum[31:28], c_out, a[31:28], b[31:28], c[6]);

endmodule


module bit4_CLA(sum, c_out, a, b, c_in); 

    input [3:0] a, b; // 4비트 연산일 때
    input c_in;
    output [3:0] sum;
    output c_out;

    wire [2:0] c;

    CLA cla1 (sum[0], c[0], a[0], b[0], c_in);
    CLA cla2 (sum[1], c[1], a[1], b[1], c[0]);
    CLA cla3 (sum[2], c[2], a[2], b[2], c[1]);
    CLA cla4 (sum[3], c_out, a[3], b[3], c[2]);

endmodule

module CLA(sum, c_out, a, b, c_in);

    input a, b, c_in;
    output sum, c_out;

    wire g, p;

    assign g = a && b;
    assign p = (~a && b) || (a && ~b);

    assign c_out = g || (c_in && p);
    assign sum = (~p && c_in) || (p && ~c_in);

endmodule