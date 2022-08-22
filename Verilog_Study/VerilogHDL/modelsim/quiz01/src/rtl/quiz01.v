`timescale 1ns/1ps

module quiz01 (clk, rst_n, in0, in1);

    input clk, rst_n;
    output reg in0, in1;

    reg [1:0] c_state, n_state;

    parameter S_0 = 2'b00;
    parameter S_1 = 2'b01;
    parameter S_2 = 2'b10;
    parameter S_3 = 2'b11;

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
    S_3: n_state = S_0;
    default: n_state = S_0;
    endcase

    always @ (c_state)
    begin
        in0 = c_state[1];
        in1 = c_state[0];
    end

endmodule

module input2_and (in0, in1, out);

    input in0, in1;
    output out;

    assign out = in0 && in1;

endmodule

