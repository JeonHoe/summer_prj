# 2차원 리스트 알아보기 쉽게 만들기
a = [[10, 20], [30, 40], [50, 60]]
print(a)

from pprint import pprint
pprint(a, indent=4, width=20)

print() # 줄 바꿈을 위한 코드

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0  for j in range(2)] for i in range(3)]
print(a)
b = [[0] * 2 for i in range(3)]
print(b)

print() # 줄 바꿈을 위한 코드

# sorted로 2차원 리스트 정렬하기
students = [['John', 'C', 19], ["Maria", 'A', 25], ['Andrew', 'B', 7]]
print(sorted(students, key=lambda student : student[1])) # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student : student[2])) # 안쪽 리스트의 인덱스 2을 기준으로 정렬

print() # 줄 바꿈을 위한 코드

# 2차원 리스트 복사
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b) # 2차원 리스트는 copy를 사용해도 완전히 복사되지 않는다
import copy
a = [[10, 20], [30, 40]]
b = copy.deepcopy(a) # 완전히 복사하기 위해선 copy 모듈 안에 deepcopy 메서드를 사용해야 한다
b[0][0] = 500
print(a)
print(b)
