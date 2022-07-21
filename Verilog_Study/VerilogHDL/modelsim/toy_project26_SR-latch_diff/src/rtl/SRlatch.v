module SR_latch(q, qb, s, r, reset);

    input s, r, reset;
    output reg q, qb;

    wire Q, Qb;
    
    assign Q = (reset == 1'b1) ? 1'b0 : !(!s && Qb);
    assign Qb = (reset == 1'b1) ? 1'b1 : !(~r && Q);
    
    always @ (s, r, reset)
    begin
        q = Q;
        qb = Qb;
    end
    

endmodule

