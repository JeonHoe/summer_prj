// 모듈

// Verilog의 기본적인 구조 블록 단위는 모듈이다.
// 모듈 정의 처음에는 모듈 이름 포트 리스트, 포트 선언, 그리고 선택적으로 피라미터가 온다.
// 포트 리스트와 포트 선언은 외부 환경과 연결할 때만 쓴다.
// 모듈은 5가지 -변수 선언, 데이터플로우 문, 하위 모듈의 파생, 행위적 블록, 그리고 태스크 또는 함수- 성분으로 구성.
// 모듈 정의에서 성분들은 모듈을 정의할 때, 어떤 순서나 어떤 지점에 나타나도 상관없다.
// 하지만 시작은 module로 시작해, endmodule로 끝나야 한다.

// SR 래치

// 모듈 이름과 포트 리스트 선언
module SR_latch (Q, Qbar, Sbar, Rbar);

    // 포트 선언
    output Q, Qbar;
    input Sbar, Rbar;

    // 하위 모듈 파생.
    // wire가 꼬인 형태로 연결되어 있음을 주목.
    nand n1 (Q, Sbar, Qbar);
    nand n2 (Qbar, Rbar, Q);


endmodule
// endmodule문

// 모듈 이름과 포스트 리스트
// 스티뮬러스 모듈 (testbench)
module Top;

// wire, reg 선언
wire q, qbar;
reg set, reset;

// 하위 모듈의 파생.
// 이 경우 SR 래치를 파생.
// SR 래치에 invert된 set과 reset 신호를 공급.
SR_latch m1 (q, qbar, ~set, ~reset);

// 행위적 블록, initial
initial
begin
    $monitor($time, "set = %b, reset = %b, q = %b\n", set, reset, q);
    set = 0, reset = 0;
    #5 reset = 1;
    #5 reset = 0;
    #5 set = 1;
end

endmodule

