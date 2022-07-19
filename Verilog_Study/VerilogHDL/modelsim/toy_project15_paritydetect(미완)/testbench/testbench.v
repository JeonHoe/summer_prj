module testbench();

  reg a, b, c;
  wire p_odd, p_even;

  parity p1 (p_odd, p_even, a, b, c);

  initial
  begin
    a = 1'b0; b = 1'b0; c = 1'b0;
    #10 a = 1'b0; b = 1'b0; c = 1'b1;
    #10 a = 1'b0; b = 1'b1; c = 1'b0;
    #10 a = 1'b0; b = 1'b1; c = 1'b1;
    #10 a = 1'b1; b = 1'b0; c = 1'b0;
    #10 a = 1'b1; b = 1'b0; c = 1'b1;
    #10 a = 1'b1; b = 1'b1; c = 1'b0;
    #10 a = 1'b1; b = 1'b1; c = 1'b1;
    #10 $stop;
  end

endmodule