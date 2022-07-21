module testbench();
    
    reg a, b, c_in;
    wire sum, c_out;

    fulladd fa1(sum, c_out, a, b, c_in);

    initial
    begin
        a = 1'b0; b = 1'b0; c_in = 1'b0;
        #10 a = 1'b0; b = 1'b0; c_in = 1'b1;
        #10 a = 1'b0; b = 1'b1; c_in = 1'b0;
        #10 a = 1'b0; b = 1'b1; c_in = 1'b1;
        #10 a = 1'b1; b = 1'b0; c_in = 1'b0;
        #10 a = 1'b1; b = 1'b0; c_in = 1'b1;
        #10 a = 1'b1; b = 1'b1; c_in = 1'b0;
        #10 a = 1'b1; b = 1'b1; c_in = 1'b1;
        #10 $stop;
    end

endmodule