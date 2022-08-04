module  register_diff(out, d_in, clk, reset); // 직렬 입력 - 병렬 출력

    input d_in, clk, reset;
    output reg [3:0] out;

    reg [3:0] q;

    always @ (posedge clk, negedge reset)
    begin
        if (!reset)
        begin
            q <= 0;
        end
        else
        begin
            q[0] <= q[1];
            q[1] <= q[2];
            q[2] <= q[3];
            q[3] <= d_in;
        end
    end

    always @(q) out = q;

endmodule
