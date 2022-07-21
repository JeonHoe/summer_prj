module testbench();
    
    reg [1:0] a, b;
    wire g, e, l;

    comparator cmp1(g, e, l, a, b);

    initial
    begin
        a = 2'b00; b = 2'b00;
        #10 a = 2'b00; b = 2'b01;
        #10 a = 2'b00; b = 2'b10;
        #10 a = 2'b00; b = 2'b11;
        #10 a = 2'b01; b = 2'b00;
        #10 a = 2'b01; b = 2'b01;
        #10 a = 2'b01; b = 2'b10;
        #10 a = 2'b01; b = 2'b11;
        #10 a = 2'b10; b = 2'b00;
        #10 a = 2'b10; b = 2'b01;
        #10 a = 2'b10; b = 2'b10;
        #10 a = 2'b10; b = 2'b11;
        #10 a = 2'b11; b = 2'b00;
        #10 a = 2'b11; b = 2'b01;
        #10 a = 2'b11; b = 2'b10;
        #10 a = 2'b11; b = 2'b11;
        #10 $stop;
    end

endmodule