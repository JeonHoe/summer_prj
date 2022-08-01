`timescale 1ns/1ps

module det_011_mealy(clk, reset, din, dout);

  input clk, reset, din;
  output reg dout;

  reg [1:0] c_state, n_state;
  parameter s_0 = 2'b00;
  parameter s_1 = 2'b01;
  parameter s_2 = 2'b10;

  always @(posedge clk, negedge reset)
  begin
  if (!reset)
    c_state <= 0;
  else
    c_state <= n_state;
  end

  always @(c_state, din)
  begin
    case(c_state)
    s_0:
    begin
      n_state = (din == 0) ? s_1 : c_state;
      dout = 1'b0;
    end
    s_1:
    begin
      n_state = (din == 0) ? c_state : s_2;
      dout = 1'b0;
    end
    s_2:
    begin
      n_state = (din == 0) ? s_1 : s_0;
      dout = (din == 0) ? 1'b0 : 1'b1;
    end
    default:
    begin
      n_state = s_0;
      dout = 1'b0;
    end
    endcase
  end

endmodule
