// 설계 블록이 완성되었을 때, 반드시 설계 블록을 테스트 해야 한다.
// 설계 블록의 기능적인 면은 스티뮬러스를 적용시켜 결과를 보는 것으로 테스트 가능하다.
// 이런 스티뮬러스를 적용시킬 수 있는 블록을 스티뮬러스(stimulus) 블록이라고 한다.
// 스티뮬러스 블록은 일반적으로 테스트 벤치(test bench)라 불린다.

module stimulus; // 스티뮬러스 블록 모듈 파생

reg clk;
reg reset;
wire [3:0] q;

//설계 블록 파생
ripple_carry_counter r1 (q, clk, reset);

// 설계 블록에서 나오는 clk 신호 조절. 주기 = 10
initial
    clk = 1'b0; // clk를 0으로 설정
always
    #5 clk = ~clk // 매 5 단위 시간마다 clk값을 바꾼다.

// 설계 블록에서 나오는 reset 신호를 조절.
// reset 신호는 0에서 20 그리고 200에서 220까지 참이다.
initial
begin
    reset = 1'b1;
    #15 reset = 1'b0;
    #180 reset = 1'b1;
    #10 reset = 1'b0;
    #20 $finish; // 시뮬레이션을 끝냄.
end

// 결과를 출력
initial
    $monitor ($time, "output q = %d", q);
    
endmodule
