// 1. 게이트 형태

// 논리 회로(logic circuit)는 논리 게이트를 사용해서 설계할 수 있다.
// Verilog는 기본적인 논리 게이트를 프리미티브로 미리 정의해 놓았다.
// 프리미티브는 Verilog에서 미리 정의되어 있고, 모듈 정의를 필요로 하지 않고 모듈처럼 파생 가능.
// 모든 논리 회로는 기본적인 게이트를 사용해서 설계될 수 있다.
// 기본 게이트는 and/or와 buf/not이 있다.

// 1.1 AND/OR 게이트

// And/or 게이트는 하나의 스칼라 출력과 여러 개의 스칼라 입력을 가지고 있다.
// 게이트 터미널 리스트의 첫 번째 터미널은 출력, 나머지 터미널은 입력이다.

// 사용법 : <게이트 종류> <인스턴스 이름> (출력, 입력1, 입력2, ... 입력n);

// 게이트의 출력은 입력값 중 하나가 바뀌자마자 값을 계산해 가진다.
// And/or는 다음과 같이 이용될 수 있다.

// and or xor nand nor xnor

wire OUT, IN1, IN2, IN3;

// 기본적인 게이트 파생

and a1 (OUT, IN1, IN2);
nand na1 (OUT, IN1, IN2);
or o1 (OUT, IN1, IN2);
nor nor1 (OUT, IN1, IN2);
xor x1 (OUT, IN1, IN2);
xnor nx1 (OUT, IN1, IN2);

// 두 개 이상의 입력 : 3개 입력을 가진 nand 게이트

nand na1_3inp (OUT, IN1, IN2, IN3);

// 인스턴스 이름이 없는 게이트

and (OUT, IN1, IN2); // 합법적인 게이트 파생

// 1.2 Buf/Not 게이트

// Buf/Not 게이트는 하나의 스칼라 입력과 하나 또는 그 이상의 스칼라 출력을 갖는다.
// 포트의 마지막 터미널은 입력과 연결되고, 나머지 터미널은 출력과 연결된다.

// 사용법 : <게이트 종류> <인스턴스 이름> (출력1, 출력2, ... , 입력);

// Verilog는 두 개의 프리미티브 buf/not 게이트를 제공한다.

// buf not

wire OUT1, OUT2, IN;

// 기본적인 게이트의 파생

buf b1 (OUT1, IN);
not n1 (OUT1, IN);

// 두 개 이상의 출력

buf b1_2out (OUT1, OUT2, IN);

// 인스턴스 이름이 없는 게이트 파생

not (OUT1, IN); // 합법적인 게이트 파생

// buf/not 게이트에 조절 신호를 추가한 게이트도 사용할 수 있다. -> bufif/notif

// bufif1 notif1 bufif0 notfi0

wire out, in, ctrl;

// bufif의 파생

bufif1 b1 (out, in ,ctrl);
bufif0 b0 (out, in ,ctrl);

// notif의 파생

notif1 n1 (out, in ,ctrl);
notif0 n0 (out, in ,ctrl);

// 1.3 인스턴스의 배열

// 많은 상황에서 반복된 인스턴스가 요구될 때가 있다.
// 이 인스턴스들은 오직 그들이 연관된 벡터의 인덱스에 의해 서로 구분된다.
// 그런 인스턴스들의 간단한 명세를 위해 Verilog는 정의되어 있는 프리미티브 인스턴스의 배열을 허가한다.

wire [7:0] OUT, IN1, IN2;

// 기본적인 게이트 파생

nand n_gate [7:0] (OUT, IN1, IN2);

// 위의 것은 아래의 8개를 파생한 것과 같다.

nand n_gate0 (OUT[0], IN1[0], IN2[0]);
nand n_gate1 (OUT[1], IN1[1], IN2[1]);
nand n_gate2 (OUT[2], IN1[2], IN2[2]);
nand n_gate3 (OUT[3], IN1[3], IN2[3]);
nand n_gate4 (OUT[4], IN1[4], IN2[4]);
nand n_gate5 (OUT[5], IN1[5], IN2[5]);
nand n_gate6 (OUT[6], IN1[6], IN2[6]);
nand n_gate7 (OUT[7], IN1[7], IN2[7]);
