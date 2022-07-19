module in3_nand_gate(a, b, c, out);

    input a;
    input b;
    input c;
    output out;

    assign out = ~(a && b && c);

endmodule