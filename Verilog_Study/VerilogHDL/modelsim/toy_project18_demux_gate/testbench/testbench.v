module testbench();
    
    reg [3:0] in;
    reg [2:0] sel;
    wire [3:0] out1, out2, out3, out4, out5, out6, out7, out8;

    demux dem1(in, sel, out1, out2, out3, out4, out5, out6, out7, out8);

    initial
        in = 4'b1011;

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

endmodule