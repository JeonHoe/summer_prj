// 포트

// 포트는 모듈이 외부 환경과 소통할 수 있는 인터페이스이다.
// 모듈은 오직 포트를 통해서만 외부환경과 상호 작용할 수 있다.
// 외부 환경에서는 모듈의 내부를 볼 수 없다.
// 인터페이스가 변하지 않는 한 외부 환경에 영향을 주지 않고 모듈의 내부를 수정할 수 있다.
// 포트는 터미널로 인용될 수 있다.

// 포트 나열

// 모듈 정의는 선택적인 포스트 리스트를 포함한다.
// 만약 모듈이 외부 환경과 상호 작용하지 않는다면, 모듈은 포트를 가지지 않는다.

// 포트 선언

// 포트 리스트의 모든 포트는 모듈 안에서 선언되어야 한다.
// 포트 리스트에 있는 각 포트는 input, output, inout으로 정의된다.

// Verilog에서 모든 포트 선언은 wire로 선언된다.
// output 포트가 값을 유지해야 한다면, 반드시 reg로 선언되어야 한다.

module D_FF (q, d, clk, reset);

// 출력 포트 선언
output q;
reg q; // 출력 포트 q는 값을 유지 -> reg로 선언.

// 입력 포트 선언
input d, clk, reset;

always @ (posedge clk or posedge reset)
begin
if (reset)
    q = 1'b0;
else
    q = d;
end
endmodule

// reg 변수는 값을 저장.
// 입력 포트는 값을 저장하지 않고 단순히 그것에 연결된 외부 신호에 의해 변환 값을 그대로 전달만 하면 됨.
// 따라서 input과 inout은 reg로 선언될 수 없다.

// 포트 연결 규칙

// 입력(Inputs)
// 내부적으로 입력 포트는 반드시 넷형. 외부적으로 입력 포트는 reg 또는 넷 변수와 연결될 수 있다.

// 출력(Outputs)
// 내부적으로 출력 포트는 reg 또는 넷형. 외부적으로 출력 포트는 반드시 넷과 연결되어야 한다.

// Inouts
// 내부적으로  입출력(inout) 포트는 반드시 넷형이며, 외부적으로 입출력 포트는 반드시 넷과 연결되어야 한다.

// 크기 맞춤(Width matching)
// 모듈 포트 사이에 연결할 때, Verilog는 내부와 외부 항목이 서로 다른 크기를 가지는 연결을 허용.
// 그러나 크기를 맞추지 않는 것은 좋지 않다.

// 연결되지 않는 포트
// Verilog는 포트를 연결하지 않은 채 내버려 둘 수 있다.
// 예를 들어 어떤 출력 포트가 단순히 디버그를 위한 것이라면, 그것은 외부 신호로 연결되지 않아도 상관없다.

// 외부신호에 포트 연결하기

// 모듈 파생과 모듈 정의 안에서 포트를 지정된 신호끼리 연결하는 방법은 두 가지가 존재한다.
// 이 두 방법은 혼용할 수 없다.

// 1. 위치에 의한 포트 연결

// 위치에 의한 포트 연결은 초보자들도 쉽게 알 수 있는 방법이다.
// 파생된 모듈의 포트와 정의한 모듈의 포트들은 같은 위치에 있는 신호들끼리 연결된다.

module Top;

// 연결 변수의 선언
reg A, B;
reg C_IN;
wire SUM;
wire C_OUT;

fulladd fa1 (.c_out(C_OUT), .sum(SUM), .b(B), .c_in(C_IN), .a(A),);

fulladd fa0 (SUM, C_OUT, A, B, C_IN); // 신호가 위치에 의해 연결



initial
begin
    A = 1'b0; B = 1'b0; C_IN = 1'b0;
    #10 A = 1'b0; B = 1'b1; C_IN = 1'b0;
    #10 A = 1'b1; B = 1'b0; C_IN = 1'b0;
    #10 A = 1'b1; B = 1'b1; C_IN = 1'b0;
    #10 A = 1'b0; B = 1'b0; C_IN = 1'b1;
    #10 A = 1'b0; B = 1'b1; C_IN = 1'b1;
    #10 A = 1'b1; B = 1'b0; C_IN = 1'b1;
    #10 A = 1'b1; B = 1'b1; C_IN = 1'b1;
end
initial
$monitor(&time, "SUM = %d, C_OUT = %d", SUM, C_OUT);

endmodule

module testbench();

reg d, clk, reset;
wire q;

D_FF dff1 (q, d, clk, reset);

initial
    clk = 1'b1;
always
    #5 clk = ~clk;
initial
begin
    reset = 1'b1;
    #15 reset = 1'b0;
end

initial
begin
    d = 1'b1;
    #12 d = 1'b0;
    #9 d = 4'b1;
    #15 d = 4'b0;
    #20 $stop;
end

endmodule

module fulladd (sum, c_out, a, b, c_in);

// 출력 포트 선언
output sum;
output c_out;

//입력 포트 선언
input a;
input b;
input c_in;

wire tmp = (~a&&b)||(a&&~b);

assign sum = (~tmp&&c_in)||(tmp&&c_in);
assign c_out = (a&&b)||(c_in&&a)||(c_in&&b);

endmodule

// 이름에 의한 포트 연결

// 대형 설계에서는 모듈이 약 50개의 포트를 가져, 모듈 정의에서 포트의 위치를 기억하기 어렵기 때문에 자주 에러가 발생.
// Verilog는 위치 대신 포트 이름에 의해 외부 신호를 연결할 수 있다.

fulladd fa1 (.c_out(C_OUT), .sum(SUM), .b(B), .c_in(C_IN), .a(A),);


// 이름에 의한 포트 연결의 장점은 포트 이름이 바뀌지 않는 한 모듈 파생에서 연결을 바꾸지 않고 모듈 포트 리스트의 순서를 재배치 가능.

// 계층적 이름

// Verilog는 계층적 설계방법을 지원한다.
// 모든 모듈 인스턴스, 신호와 변수는 지시어로 정의된다.
// 일부 지시어 설계 계층은 특정 자리에 위치한다.
// 계층적 이름 참조는 유일한 이름을 가지고 설계 계층에서 모든 지시어를 나타낼 수 있다.
// 계층적 이름은 각 계층 수준의 지시어 리스트를 도트(".")로 구분한다.
