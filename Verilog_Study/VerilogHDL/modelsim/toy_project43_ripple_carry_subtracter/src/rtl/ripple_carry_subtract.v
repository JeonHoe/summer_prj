module ripple_carry_subtract (res, c_out, a, b);

    input [31:0] a, b;
    output [31:0] res;
    output c_out;

    parameter sel =1;
    wire [6:0] tmp_c;
    wire [31:0] ocb; // 1의 보수화된 b

    bit4_one_complement boc1 (ocb[3:0], b[3:0], sel);
    bit4_one_complement boc2 (ocb[7:4], b[7:4], sel);
    bit4_one_complement boc3 (ocb[11:8], b[11:8], sel);
    bit4_one_complement boc4 (ocb[15:12], b[15:12], sel);
    bit4_one_complement boc5 (ocb[19:16], b[19:16], sel);
    bit4_one_complement boc6 (ocb[23:20], b[23:20], sel);
    bit4_one_complement boc7 (ocb[27:24], b[27:24], sel);
    bit4_one_complement boc8 (ocb[31:28], b[31:28], sel);

    ripple_carry_add rca1 (res, c_out, a, ocb, sel);

endmodule

module ripple_carry_add (sum, c_out, a, b, c_in);

    input [31:0] a, b;
    input c_in;
    output [31:0] sum;
    output c_out;

    wire [6:0] tmp_c;

    bit4_fulladd b4fa1 (sum[3:0], tmp_c[0], a[3:0], b[3:0], c_in);
    bit4_fulladd b4fa2 (sum[7:4], tmp_c[1], a[7:4], b[7:4], tmp_c[0]);
    bit4_fulladd b4fa3 (sum[11:8], tmp_c[2], a[11:8], b[11:8], tmp_c[1]);
    bit4_fulladd b4fa4 (sum[15:12], tmp_c[3], a[15:12], b[15:12], tmp_c[2]);
    bit4_fulladd b4fa5 (sum[19:16], tmp_c[4], a[19:16], b[19:16], tmp_c[3]);
    bit4_fulladd b4fa6 (sum[23:20], tmp_c[5], a[23:20], b[23:20], tmp_c[4]);
    bit4_fulladd b4fa7 (sum[27:24], tmp_c[6], a[27:24], b[27:24], tmp_c[5]);
    bit4_fulladd b4fa8 (sum[31:28], c_out, a[31:28], b[31:28], tmp_c[6]);

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

module fulladd(sum, c_out, a, b, c_in);

    input a, b, c_in;
    output sum, c_out;

    assign sum = (~a && ~b && c_in) || (~a && b && ~c_in) || (a && ~b && ~c_in) || (a&&b&&c_in);
    assign c_out = a && b  || ((a^b) && c_in);

endmodule

module bit4_one_complement(f, x, w);

    input [3:0] x;
    input w;
    output [3:0] f;
    
    one_complement oc1 (f[3], x[3], w);
    one_complement oc2 (f[2], x[2], w);
    one_complement oc3 (f[1], x[1], w);
    one_complement oc4 (f[0], x[0], w);

endmodule

module one_complement(f, x, w);

    input x, w;
    output f;
    
    assign f = x ^ w;

endmodule