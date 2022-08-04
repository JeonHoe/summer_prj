module  register(out, d_in, ld, clk, reset); // 병렬 입력 - 직렬 출력

    input ld, clk, reset;
    input [3:0] d_in;
    output reg out;

    reg [3:0] q;

    always @ (posedge ld, posedge clk, negedge reset)
    begin
        if (reset == 0 && ld == 0)
        begin
            q = 0;
            out = 0;
        end
        else if (reset == 1 && ld == 1)
        begin
            q <= d_in;
            out <= d_in[0];
        end
        else
        begin
        out <= q[0];
        q[0] <= q[1];
        q[1] <= q[2];
        q[2] <= q[3];
        end
    end

    always @ (q)
    begin
        
    end

endmodule
