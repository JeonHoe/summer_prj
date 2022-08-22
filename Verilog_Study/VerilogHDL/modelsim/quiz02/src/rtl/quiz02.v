`timescale 1ns/1ps

module quiz02 (clk, rst_n, in0, in1);

    input clk, rst_n;
    output reg in0, in1;

    reg [1:0] c_state, n_state;

    integer count;

    parameter step = 5;

    parameter S_0 = 2'b00;
    parameter S_1 = 2'b01;
    parameter S_2 = 2'b10;
    parameter S_3 = 2'b11;

    always @ (posedge clk, negedge rst_n)
    begin
        if (!rst_n) 
        begin
            count <= 0;
            c_state <= 2'b0;
        end
        else count = count + 1;
    end

    always @ (count)
    begin
        if (!(count%step) && count) 
        begin
            c_state <= n_state;
            count = 0;
        end
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