module JK_ff(q, qb, j, k, clk, reset); 

    input j, k, reset, clk;
    output reg q, qb;

    always @(posedge clk,  posedge reset)
    begin
        if (reset)
        begin
            q = 1'b0; qb = 1'b1;
        end
        else if (j == 1'b0 && k == 1'b0)
        begin
            q <= q; qb <= qb; 
        end
        else if (j == 1'b0 && k == 1'b1)
        begin
            q <= 1'b0; qb <= 1'b1;
        end
        else if (j == 1'b1 && k == 1'b0)
        begin
            q <= 1'b1; qb <= 1'b0;
        end
        else
        begin
            q <= qb; qb <= q;
        end
    end
    

endmodule

