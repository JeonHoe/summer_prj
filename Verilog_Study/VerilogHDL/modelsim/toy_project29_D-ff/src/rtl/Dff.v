module D_ff(q, qb, d, clk, reset);

    input d, clk, reset;
    output q, qb;
    reg q, qb;
    
    always @ (posedge clk, posedge reset)
        begin
            if (reset)
            begin
                q <= 1'b0; qb <= 1'b1;
            end
            else if (d == 1'b0)
            begin
                q <= 1'b0; qb <= 1'b1;
            end
            else
            begin
                q <= 1'b1; qb = 1'b0;
            end
        end

endmodule

