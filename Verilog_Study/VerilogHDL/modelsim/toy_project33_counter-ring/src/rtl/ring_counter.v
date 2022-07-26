module  ring_counter(out, clk, reset);

    input clk, reset;
    output reg [2:0] out;

    wire [2:0] q;

    D_ff dff1 (q[2], , !q[1], clk, reset);
    D_ff dff2 (q[1], , q[2], clk, reset);
    D_ff_n dff3 (q[0], , q[1], clk, reset);

    always @ (q)
        begin
                out[2] <= q[2];
                out[1] <= q[1];
                out[0] <= q[0];
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

module D_ff_n(q, qb, d, clk, set);

    input d, clk, set;
    output q, qb;
    reg q, qb;
    
    always @ (posedge clk, negedge set)
        begin
            if (!set)
            begin
                q <= 1'b1; qb <= 1'b0;
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
