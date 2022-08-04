module add_shift_multiplier (p, x, y); // 4비트 연산

    input [3:0] x, y;
    output [7:0] p;

    reg [4:0] a = 5'b0;
    reg [3:0] n = 4'b0100;
    reg [8:0] tt;

    always @ (x)
    begin
        tt = {a, y};
        while (n)
        begin
            if(tt[0] == 1)
            begin
            tt[8:4] = tt[8:4] + x;
            end
            tt = tt >> 1;
            n = n-1;
        end
    end

    assign p = tt[7:0];

endmodule