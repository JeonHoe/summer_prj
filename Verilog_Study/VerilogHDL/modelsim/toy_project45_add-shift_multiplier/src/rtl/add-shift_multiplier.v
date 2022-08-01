module bit4_SASM (product, a, b);

    input [3:0] a, b;
    output [7:0] product;

    wire [7:0] tmp1, tmp2, tmp3, tmp4;
    wire [7:0] tmp_s1, tmp_s2, tmp_s3;
    wire [2:0] tmp_c;
    wire [7:0] p1, p2;

    mux m1 (tmp1, 4'b0, a, b[0]);
    mux m2 (tmp2, 4'b0, a, b[1]);
    shifter shft1 (tmp_s1, tmp2, 2'b01);
    mux m3 (tmp3, 4'b0, a, b[2]);
    shifter shft2 (tmp_s2, tmp3, 2'b10);
    mux m4 (tmp4, 4'b0, a, b[3]);
    shifter shft3 (tmp_s3, tmp4, 2'b11);

    bit8_fulladd b8fa1 (p1, tmp_c[0], tmp1, tmp_s1, 0);
    bit8_fulladd b8fa2 (p2, tmp_c[1], p1, tmp_s2, tmp_c[0]);
    bit8_fulladd b8fa3 (product, tmp_c[2], p2, tmp_s3, tmp_c[1]);

endmodule

module bit8_fulladd(sum, c_out, a, b, c_in); 

    input [7:0] a, b;
    input c_in;
    output [7:0] sum;
    output c_out;

    wire tmp_c;

    bit4_fulladd fa1 (sum[3:0], tmp_c, a[3:0], b[3:0], c_in);
    bit4_fulladd fa2 (sum[7:4], c_out, a[7:4], b[7:4], tmp_c);

endmodule

module bit4_fulladd(sum, c_out, a, b, c_in); 

    input [3:0] a, b; // 4비트 연산일 때
    input c_in;
    output [3:0] sum;
    output c_out;

    wire [2:0] tmp_c;

    fulladd fa1 (sum[0], tmp_c[0], a[0], b[0], c_in);
    fulladd fa2 (sum[1], tmp_c[1], a[1], b[1], tmp_c[0]);
    fulladd fa3 (sum[2], tmp_c[2], a[2], b[2], tmp_c[1]);
    fulladd fa4 (sum[3], c_out, a[3], b[3], tmp_c[2]);

endmodule

module fulladd (sum, c_out, a, b, c_in);

    input a, b, c_in;
    output sum, c_out;

    assign sum = (~a && ~b && c_in) || (~a && b && ~c_in) || (a && ~b && ~c_in) || (a && b && c_in);
    assign c_out = a && b  || ((a^b) && c_in);

endmodule

module mux (out, in1, in2, sel);

    input [3:0] in1, in2;
    input sel;
    output [7:0] out;

    assign out = (sel == 0) ? in1 :
                 (sel == 1) ? in2 : 4'bx;

endmodule

module shifter (out, in, num);

    input [3:0] in;
    input [1:0] num;
    output [7:0] out;

    assign out = in << num;

endmodule
