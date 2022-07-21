module D_latch(q, qb, d, reset); 

    input d, reset;
    output q, qb;
    reg q, qb;
    
    always @ (d, reset)
        begin
            if (reset == 1'b1)
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

