module twos_complement_subtract (diff, c_out, a, b);

    input a, b;
    output diff, c_out;

    wire ocb;

    one_complement oc1 (ocb, b, 1'b1);
    fulladd fa1 (diff, c_out, a, ocb, 1'b1);

endmodule

module fulladd(sum, c_out, a, b, c_in);

    input a, b, c_in;
    output sum, c_out;

    assign sum = (~a && ~b && c_in) || (~a && b && ~c_in) || (a && ~b && ~c_in) || (a&&b&&c_in);
    assign c_out = a && b  || ((a^b) && c_in);

endmodule



module one_complement(f, x, w);

    input x, w;
    output f;
    
    assign f = x ^ w;

endmodule