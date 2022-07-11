module testbench();
    
    reg a;
    reg b;
    reg c;
    wire out;

    in3_xor_gate i3_xog(a, b, c, out);

    initial
    begin
        a = 1'b0; b = 1'b0; c = 1'b0;
        #10; a = 1'b0; b = 1'b0; c = 1'b1;
        #10; a = 1'b0; b = 1'b1; c = 1'b0;
        #10; a = 1'b0; b = 1'b1; c = 1'b1;
        #10; a = 1'b1; b = 1'b0; c = 1'b0;
        #10; a = 1'b1; b = 1'b0; c = 1'b1;
        #10; a = 1'b1; b = 1'b1; c = 1'b0;
        #10; a = 1'b1; b = 1'b1; c = 1'b1;
        #10; $stop;
    end

endmodule