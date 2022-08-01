module  register(out, d_in, ld, clk, reset); // 병렬 입력 - 직렬 출력

    input ld, clk, reset;
    input [3:0] d_in;
    output reg out;

    wire [3:0] q, qb;

    D_ff dff1 (q[3], qb[3], 0, clk, ~(ld && d_in[0]), reset);
    D_ff dff2 (q[2], qb[2], q[3], clk, ~(ld && d_in[1]), reset);
    D_ff dff3 (q[1], qb[1], q[2], clk, ~(ld && d_in[2]), reset);
    D_ff dff4 (q[0], qb[0], q[1], clk, ~(ld && d_in[3]), reset);
    
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
