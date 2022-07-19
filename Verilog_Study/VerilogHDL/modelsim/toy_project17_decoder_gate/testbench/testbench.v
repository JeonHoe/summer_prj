module testbench();
    
    reg [2:0] in;
    wire out1, out2, out3, out4, out5, out6, out7, out8;

    decoder dec1 (in, out1, out2, out3, out4, out5, out6, out7, out8);

    initial
    begin
        in = 3'o0;
        #10 in = 3'o1;
        #10 in = 3'o2;
        #10 in = 3'o3;
        #10 in = 3'o4;
        #10 in = 3'o5;
        #10 in = 3'o6;
        #10 in = 3'o7;
        #10; $stop;
    end

endmodule