module  register_diff2(out, pd_in, d_in, ld, clk, reset); // (직렬 입력 + 병렬 입력) - 직렬 출력

    input d_in, ld, clk, reset;
    input [3:0] pd_in;
    output reg out;

    reg [3:0] q;

    always @ (posedge ld, posedge clk, negedge reset)
    begin
        if (reset == 0 && ld == 0)
        begin
            q = 0;
        end
        else if (reset == 1 && ld == 1)
        begin
            q <= pd_in;
        end
        else
        begin
        q[0] <= q[1];
        q[1] <= q[2];
        q[2] <= q[3];
        q[3] <= d_in;
        end
    end

    always @ (q) out = q[0];

endmodule
