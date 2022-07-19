module testbench();
    
    reg a, b;
    wire g, e, l;

    equal e1(e, a, b);
    greater g1(g, a, b);
    less l1(l, a, b);

    initial
    begin
        a = 1'b0; b = 1'b0;
        #10 a = 1'b0; b = 1'b1;
        #10 a = 1'b1; b = 1'b0;
        #10 a = 1'b1; b = 1'b1;
        #10 $stop;
    end

endmodule