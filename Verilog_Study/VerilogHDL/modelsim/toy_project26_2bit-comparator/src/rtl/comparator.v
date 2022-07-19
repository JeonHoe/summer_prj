module comparator(g, e, l, a, b); // 2비트 비교기

    input [1:0] a, b;
    output g, e, l;

    wire [1:0] tmp;

    equal e1(tmp[0], a[0], b[0]);
    equal e2(tmp[1], a[1], b[1]);
    assign e = tmp[1] && tmp[0];
    assign g = a[1] && !b[1] || (tmp[1] && (a[0] && !b[0]));
    assign l = (!a[1] && b[1]) || (tmp[1] && (!a[0] && b[0]));
    

endmodule

module equal(e, a, b);
    
    input a, b;
    output e;

    assign e = !((!a && b) || (a && !b));

endmodule
