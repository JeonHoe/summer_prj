# 람다 표현식으로 함수 만들기
def plus_ten(n):
    return n + 10
print(plus_ten(1))

p_ten = lambda x: x + 10
print(p_ten(1))

print()

# 람다 표현식 자체를 호출하기
print((lambda x:x+10)(1))

print()

# 람다 표현식 안에는 변수 생성 불가능
# 따라서 람다 표현식 바깥에서 변수를 선언하고 사용
y = 10
print((lambda x:x + y)(1))

print()

# 람다 표현식 인수로 사용하기
def mul_ten(x):
    return x * 10

print(list(map(mul_ten, [1, 2, 3])))
print(list(map((lambda x:x * 10), [1, 2, 3])))

print()

# 참고 : 람다 표현식으로 매개변수가 없는 함수 만들기
print((lambda : 1)())
# 람다 표현식으로 매개변수가 없는 함수를 만들 때는 lambda 뒤에 아무것도 지정하지 않고 :(콜론)을 붙인다.
# 단 :(콜론) 뒤에는 반드시 반환활 값이 있어야 한다. 표현식은 반드시 값으로 평가되어야 하기 때문에.

print()

# 람다 표현식과 map, filter, reduce 함수 활용하기

# 람다 표현식에 조건부 표현식 사용하기
# lambda 매개변수들: 식1 if 조건식 else 식2
# 반드시 else를 사용해야 한다. 그렇지 않을 경우 에러가 출력된다.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if  x % 3 == 0 else x, a)))
# elif문을 사용할 수 없으므로 대신에 if를 연속으로 사용한다.
print(list(map(lambda x:str(x) if x==1 else float(x) if x == 2 else x + 10 ,a)))
# 위 문장은 아래 함수와 같다.
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
print(list(map(f, a)))

print()

# map에 객체들 여러 개 넣기
# map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수 있다.
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

print(list(map(lambda x, y: x * y, a, b)))

# filter 사용하기
# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져온다.
# filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져온다.
def f(x):
    return x > 5 and x < 10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(a)
print(list(map(f, a)))
print(list(filter(f, a)))

print(list(filter(lambda x: x>5 and x<10, a)))

print()

# reduce 사용하기
# reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수이다.
def f(x, y):
    return x + y
a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(f, a))
print(reduce(lambda x, y: x + y, a))
