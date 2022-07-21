module halfadd(sum, c_out, a, b);

    input a, b;
    output sum, c_out;

    assign sum = (~a && b) || (a && ~b);
    assign c_out = (a && b);

endmodule