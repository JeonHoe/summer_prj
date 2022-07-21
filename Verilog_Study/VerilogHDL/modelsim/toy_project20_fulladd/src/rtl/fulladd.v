module fulladd(sum, c_out, a, b, c_in);

    input a, b, c_in;
    output sum, c_out;

    assign sum = (~a && ~b && c_in) || (~a && b && ~c_in) || (a && ~b && ~c_in) || (a&&b&&c_in);
    assign c_out = a && b  || ((a^b) && c_in);

endmodule