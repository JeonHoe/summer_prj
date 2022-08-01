module  shift_register(out, d_in, ld, sl, sr, reset);

    input ld, sl, sr, reset;
    input [3:0] d_in;
    output reg [3:0] out;

    wire [3:0] q, qb;
    wire [3:0] d;

    assign d[3] = sl && q[2];
    assign d[2] = (sl && q[1]) || (sr && q[3]);
    assign d[1] = (sl && q[0]) || (sr && q[2]);
    assign d[0] = sr && q[1];


    D_ff dff1 (q[3], qb[3], d[3], ((sl && ~sr) || (~sl && sr)), ~(ld && d_in[3]), reset);
    D_ff dff2 (q[2], qb[2], d[2], ((sl && ~sr) || (~sl && sr)), ~(ld && d_in[2]), reset);
    D_ff dff3 (q[1], qb[1], d[1], ((sl && ~sr) || (~sl && sr)), ~(ld && d_in[1]), reset);
    D_ff dff4 (q[0], qb[0], d[0], ((sl && ~sr) || (~sl && sr)), ~(ld && d_in[0]), reset);
    
    always @ (q) 
    begin
        out[3] = q[3];
        out[2] = q[2];
        out[1] = q[1];
        out[0] = q[0];
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

