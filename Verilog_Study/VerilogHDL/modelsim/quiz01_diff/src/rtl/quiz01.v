`timescale 1ns/1ps

module quiz01_diff (clk, rst_n, in0, in1, in2); // 4비트

    input clk, rst_n;
    output reg in0, in1, in2;

    reg [2:0] c_state, n_state;

    parameter S_0 = 3'b000;
    parameter S_1 = 3'b001;
    parameter S_2 = 3'b010;
    parameter S_3 = 3'b011;
    parameter S_4 = 3'b100;
    parameter S_5 = 3'b101;
    parameter S_6 = 3'b110;
    parameter S_7 = 3'b111;

    always @ (posedge clk, negedge rst_n)
    begin
        if (!rst_n) c_state <= 2'b0;
        else c_state <= n_state;
    end

    always @ (c_state)
    case (c_state)
    S_0: n_state = S_1;
    S_1: n_state = S_2;
    S_2: n_state = S_3;
    S_3: n_state = S_4;
    S_4: n_state = S_5;
    S_5: n_state = S_6;
    S_6: n_state = S_7;
    S_7: n_state = S_0;
    default: n_state = S_0;
    endcase

    always @ (c_state)
    begin
        in0 = c_state[2];
        in1 = c_state[1];
        in2 = c_state[0];
    end

endmodule

module input3_and (in0, in1, in2, out);

    input in0, in1, in2;
    output out;

    assign out = in0 && in1 && in2;

endmodule
