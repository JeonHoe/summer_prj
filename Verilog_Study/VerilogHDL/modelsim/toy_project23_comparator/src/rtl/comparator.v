module equal(e, a, b);
    
    input a, b;
    output e;

    assign e =!((!a && b) || (a && !b));

endmodule

module greater(g, a, b);

    input a, b;
    output g;

    assign g = a && !b;

endmodule

module less(l, a, b);

    input a, b;
    output l;

    assign l = !a && b;

endmodule