# 연습문제
import turtle as t

n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(360/n*2)
    t.forward(100)
    t.left(360/n)

t.clear() # 거북이 그래픽 창을 지워 기존 그림 없애기

# 심사문제
n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.forward(100)
    t.right(360/n*2)
    t.forward(100)
    t.left(360/n)

t.mainloop()