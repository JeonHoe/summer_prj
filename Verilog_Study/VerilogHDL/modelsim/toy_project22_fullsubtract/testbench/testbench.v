module testbench();
    
    reg a, b, b_in;
    wire diff, b_out;

    fullsubtract fs1(diff, b_out, a, b, b_in);

    initial
    begin
        a = 1'b0; b = 1'b0; b_in = 1'b0;
        #10 a = 1'b0; b = 1'b0; b_in = 1'b1;
        #10 a = 1'b0; b = 1'b1; b_in = 1'b0;
        #10 a = 1'b0; b = 1'b1; b_in = 1'b1;
        #10 a = 1'b1; b = 1'b0; b_in = 1'b0;
        #10 a = 1'b1; b = 1'b0; b_in = 1'b1;
        #10 a = 1'b1; b = 1'b1; b_in = 1'b0;
        #10 a = 1'b1; b = 1'b1; b_in = 1'b1;
        #10 $stop;
    end

endmodule