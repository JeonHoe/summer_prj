module testbench();
  reg a;
  wire out;

  not_gate ng(a, out);

  initial
  begin
    a = 1'b0;
    #10; a = 1'b1;
    #10; $stop;
  end

endmodule