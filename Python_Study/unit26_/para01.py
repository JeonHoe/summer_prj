# 세트 만들기
# 1. 세트 = {값1, 값2, ...}
fruit = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruit)
# 세트 내에 요소들은 순서가 없고 중복이 없다
fruit = {'orange', 'orange', 'cherry'}
print(fruit)
# 순서가 없기 때문에 리스트와 요소처럼 대괄호([])로 요소를 출력할 수 없다
# 2. set(반복가능개체)
a = set('apple')
print(a)

print() # 줄 바꿈을 위한 코드

# 세트 내에 특정 값 유무 확인
fruit = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# 값 in 세트
print('orange' in fruit)
# 값 not in 세트
print('apple' not in fruit)

print() # 줄 바꿈을 위한 코드

# 집합 연산자 사용
# 합집합
# or 연산자(|) 사용
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)
# set.union 사용
print(set.union(a, b))

print() # 줄 바꿈을 위한 코드

# 교집합
# and 연산자(&) 사용
print(a&b)
# set.intersection 사용
print(set.intersection(a, b))

print() # 줄 바꿈을 위한 코드

# 차집합
# 뺄셈 연산자(-) 사용
print(a-b)
# set.difference 사용
print(set.difference(a,b))

print() # 줄 바꿈을 위한 코드

# 대칭차집합
# xor 연산자(^) 사용
print(a^b)
# set.symmetric_difference 사용
print(set.symmetric_difference(a,b))

print() # 줄 바꿈을 위한 코드

# 프로즌 세트
# 파이썬은 변경할 수 없는 세트도 제공
# 프로즌세트 = frozenset(반복가능개체)
a = frozenset(range(10))
# 프로즌세트 선언된 세트는 집합 연산으로 값을 추가하거나 제거할 수 없다
