module SR_ff(q, qb, s, r, clk, reset); 

    input s, r, reset, clk;
    output reg q, qb;

    always @(posedge clk,  posedge reset)
    begin
        if (reset)
        begin
            q <= 1'b0; qb <= 1'b1;
        end
        else if (s == 1'b0 && r == 1'b0)
        begin
            q <= q; qb <= qb; 
        end
        else if (s == 1'b0 && r == 1'b1)
        begin
            q <= 1'b0; qb <= 1'b1;
        end
        else if (s == 1'b1 && r == 1'b0)
        begin
            q <= 1'b1; qb <= 1'b0;
        end
        else
        begin
            q <= 1'b1; qb <= 1'b1;
        end
    end
    

endmodule

