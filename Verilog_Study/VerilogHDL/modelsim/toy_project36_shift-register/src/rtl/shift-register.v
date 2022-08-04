module  shift_register(out, d_in, clk, ld, sl, sr, reset);

    input clk, ld, sl, sr, reset;
    input [3:0] d_in;
    output reg [3:0] out;

    always @ (posedge clk, negedge reset)
    if (reset == 0) out = 4'b0;
    
    always @ (posedge clk, posedge ld)
    begin
    if (ld) out = d_in;
    else out = out;
    end

    always @ (posedge clk, posedge sl, posedge sr)
    begin
    if (sl == 1 && sr == 0)
    begin
        out[3] <= out[2];
        out[2] <= out[1];
        out[1] <= out[0];
        out[0] <= 0;
    end
    else if (sl == 0 && sr == 1)
    begin
        out[0] <= out[1];
        out[1] <= out[2];
        out[2] <= out[3];
        out[3] <= 0;
    end
    else out = out;
    end

endmodule

