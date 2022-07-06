import turtle as t
# 다각형 색칠하고 그리기
t.shape('turtle')
t.color('red') # 다각형 색깔 정하기
n = int(input()) # 다각형 변의 개수 입력
t.begin_fill() # 색칠할 영역 시작
for i in range(n):
    t.forward(100)
    t.left(360/n)
t.end_fill() # 색칠할 영역 끝

t.clear() # 거북이 그래픽 창을 지워 기존 그림 없애기

# 선으로 복잡한 무늬 그리기
t.shape('turtle')
t.speed('fastest') # 거북이 속도를 가장 빠른 속도로 설정
for i in range(300):
    t.forward(i)
    t.right(91)

t.mainloop() # t.done() 사용 동일

