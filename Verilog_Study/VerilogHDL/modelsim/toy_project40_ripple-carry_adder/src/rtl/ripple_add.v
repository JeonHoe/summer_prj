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