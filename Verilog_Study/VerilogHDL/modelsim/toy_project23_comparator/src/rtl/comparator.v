module comparater(e, g, l, a, b);
    
    input a, b;
    output e, g, l;

    assign e =!((!a && b) || (a && !b));
    assign g = a && !b;
    assign l = !a && b;

endmodule