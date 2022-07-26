# 클로저 사용하기
def calc():
    a = 3
    b = 5
    def mal_add(x):
        return a * x + b # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mal_add       # mul_add 함수를 반환

c = calc()
print(c(1), c(2), c(3))
# 위처럼 함수를 호출할 때 다시 꺼내 사용하는 함수를 클로저라고 한다.

print()

# lambda로 클로저 만들기
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b

c = calc()
print(c(1), c(2), c(3))

print()

# 클로저의 지역변수 변경하기
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)
c(2)
c(3)

