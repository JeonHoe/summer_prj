module SR_latch(q, q_bar, s, r, reset); 

    input s, r, reset;
    output q, q_bar;
    reg q, q_bar;
    
    always @ (s, r, reset)
        begin
            if (reset)
            begin
                q <= 1'b0; q_bar <= 1'b1;
            end
            else if (s == 1'b0 && r == 1'b0)
            begin
            q <= q; q_bar <= q_bar; 
            end
            else if (s == 1'b0 && r == 1'b1)
            begin
            q <= 1'b0; q_bar <= 1'b1;
            end
            else if (s == 1'b1 && r == 1'b0)
            begin
            q <= 1'b1; q_bar <= 1'b0;
            end
            else
            begin
            q <= 1'b1; q_bar <= 1'b1;
            end
        end

endmodule

