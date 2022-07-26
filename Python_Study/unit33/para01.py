# nonlocal과 global

# 함수 밖에 변수인 전역변수를 함수 안에서 변경하고자 할 때 global을 사용한다.

x = 10
def f():
    x = 20
    print(x)
print('1 -> ', end='')
f() # 20 출력
print('2 -> ', end='')
print(x) # 10 출력

y = 10
def f00():
    global y
    y = 20
    print(y)

print('3 -> ', end='')
f00() # 20 출력, 함수에 사용으로 전역변수 y의 값이 20으로 바뀜
print('4 -> ', end='')
print(y) # 20 출력

print()

# 함수 안에 함수를 선언해 지역변수를 변경하고자 할 때 nonlocal를 사용한다.
def A():
    a = 10
    def B():
        a = 20
    B()
    print(a)

A() # 10 출력

def A():
    a = 10
    def B():
        nonlocal a
        a = 20
    B()
    print(a)

A() # 20 출력

print()

# nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운 함수부터 먼저 찾는다
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()

A()
