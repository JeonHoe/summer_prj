module  johnson_counter(q1, q2, q3, q4, clk, reset);

    input clk, reset;
    output reg q1, q2, q3, q4;

    wire [3:0] k;

    D_ff dff1 (k[3], , !k[0], clk, reset);
    D_ff dff2 (k[2], , k[3], clk, reset);
    D_ff dff3 (k[1], , k[2], clk, reset);
    D_ff dff4 (k[0], , k[1], clk, reset);

    
    always @ (k)
        begin
            q1 <= k[3];
            q2 <= k[2];
            q3 <= k[1];
            q4 <= k[0];
        end

endmodule

module D_ff(q, qb, d, clk, reset);

    input d, clk, reset;
    output q, qb;
    reg q, qb;
    
    always @ (posedge clk, negedge reset)
        begin
            if (!reset)
            begin
                q <= 1'b0; qb <= 1'b1;
            end
            else if (d == 1'b0)
            begin
                q <= 1'b0; qb <= 1'b1;
            end
            else
            begin
                q <= 1'b1; qb <= 1'b0;
            end
        end
endmodule
