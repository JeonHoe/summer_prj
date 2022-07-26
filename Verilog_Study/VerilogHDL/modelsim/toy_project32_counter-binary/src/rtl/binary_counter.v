module  binary_counter(out, clk, reset, ud);

    input clk, reset, ud;
    output reg [3:0] out;
    
    always @ (posedge clk, posedge reset)
        begin
            if (reset)
            begin
                out = 4'b0;
            end
            else if (ud == 0)
            begin
                out <= out + 1'b1;
            end
            else
            begin
                out <= out - 1'b1;
            end
        end

endmodule

