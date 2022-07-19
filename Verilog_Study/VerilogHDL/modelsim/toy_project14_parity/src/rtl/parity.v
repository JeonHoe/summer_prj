module parity(p_odd, p_even, a, b, c);

    input a, b, c;
    output p_odd, p_even;

    assign p_even = a ^ b ^ c;
    assign p_odd = ~(a ^ b ^ c);
    
endmodule