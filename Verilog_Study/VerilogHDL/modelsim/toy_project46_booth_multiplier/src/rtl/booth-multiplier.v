module booth_multiplier (product, m, q); // 4비트

    input [3:0] m, q;
    output [7:0] product;

    booth bth (product, m, q);

endmodule

module booth (p, m, q);

    input [3:0] m, q;
    output [7:0] p;

    reg [3:0] a = 4'b0;
    wire q0 = 0;
    reg [3:0] count = 4'b0100;
    reg [8:0] tt;

    always @(m)
    begin
        tt = {a, q, q0};
        while (count)
        begin
            if ({tt[1],tt[0]} == 2'b10)
            begin
                tt[8:5] = tt[8:5] - m[3:0];
            end
            else if ({tt[1],tt[0]} == 2'b01)
            begin
                tt[8:5] = tt[8:5] + m[3:0];
            end
            if (tt[8] == 1) tt = {1'b1,tt[8:1]};
            else tt = {1'b0,tt[8:1]};
            count = count - 1;
        end
    end

    assign p = tt[8:1];

endmodule