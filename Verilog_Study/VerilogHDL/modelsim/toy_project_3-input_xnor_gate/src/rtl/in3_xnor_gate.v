module in3_xnor_gate(a, b, c, out);

    input a;
    input b;
    input c;
    output out;

    assign tmp = (~a && b) || (a && ~b);
    assign out = ~((~tmp && c) || (tmp && ~c));

endmodule