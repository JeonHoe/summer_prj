module T_ff(q, qb, t, clk, reset);

    input t, clk, reset;
    output q, qb;
    reg q, qb;
    
    always @ (posedge clk, posedge reset)
        begin
            if (reset)
            begin
                q <= 1'b0; qb <= 1'b1;
            end
            else if (t == 1'b0)
            begin
                q <= q; qb <= qb;
            end
            else
            begin
                q <= qb; qb = q;
            end
        end

endmodule

