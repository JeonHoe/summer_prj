module testbench();
    
    reg [3:0] in1, in2, in3, in4, in5, in6, in7, in8;
    reg [2:0] sel;
    wire [3:0] out;

    mux m1(out, in1, in2, in3, in4, in5, in6, in7, in8, sel);

    initial
    begin
        sel = 3'b000;
        #10 sel = 3'b001;
        #10 sel = 3'b010;
        #10 sel = 3'b011;
        #10 sel = 3'b100;
        #10 sel = 3'b101;
        #10 sel = 3'b110;
        #10 sel = 3'b111;
        #10 $stop;
    end
    initial
    begin
        in1 = 12;
        in2 = 4; 
        in3 = 7;
        in4 = 11;
        in5 = 15;
        in6 = 10;
        in7 = 8;
        in8 = 1;
    end
endmodule