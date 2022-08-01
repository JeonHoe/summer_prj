module  register_diff(out, d_in, clk, set, reset); // 직렬 입력 - 병렬 출력

    input d_in, clk, set, reset;
    output reg [3:0] out;

    wire [3:0] q;

    D_ff dff1 (q[3], , d_in, clk, set, reset);
    D_ff dff2 (q[2], , q[3], clk, set, reset);
    D_ff dff3 (q[1], , q[2], clk, set, reset);
    D_ff dff4 (q[0], , q[1], clk, set, reset);

    
    always @ (q)
        begin
            out[3] <= q[3];
            out[2] <= q[2];
            out[1] <= q[1];
            out[0] <= q[0];
        end

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

