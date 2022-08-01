module  register_diff2(out, pd_in, d_in, ld, clk, reset); // (직렬 입력 + 병렬 입력) - 직렬 출력

    input d_in, ld, clk, reset;
    input [3:0] pd_in;
    output reg out;

    wire [3:0] q, qb;
    wire [3:0] d;

    assign d[3] = ((pd_in[0] && ld) || (d_in && ~ld));
    assign d[2] = ((pd_in[1] && ld) || (q[3] && ~ld));
    assign d[1] = ((pd_in[2] && ld) || (q[2] && ~ld));
    assign d[0] = ((pd_in[3] && ld) || (q[1] && ~ld));


    D_ff dff1 (q[3], qb[3], d[3], clk, , reset);
    D_ff dff2 (q[2], qb[2], d[2], clk, , reset);
    D_ff dff3 (q[1], qb[1], d[1], clk, , reset);
    D_ff dff4 (q[0], qb[0], d[0], clk, , reset);
    
    always @ (q[0])
            out <= q[0];

endmodule

module D_ff(q, qb, d, clk, set, reset);

    input d, clk, set, reset;
    output q, qb;
    reg q, qb;
    
    always @ (posedge clk, negedge set, negedge reset)
        begin
            if (!set)
            begin
                q <= 1'b1; qb <= 1'b0;
            end
            else if (!reset)
            begin
                q <= 1'b0; qb <= 1'b1;
            end
            else if (d == 1'b0)
            begin
                q <= 1'b0; qb <= 1'b1;
            end
            else if (d == 1'b1)
            begin
                q <= 1'b1; qb <= 1'b0;
            end
        end
endmodule

