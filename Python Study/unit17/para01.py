# 반복 횟수가 정해지지 않는 반복문
import random

# randint 사용
i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i) # randint는 처음 값부터 끝 값까지의 무작위 정수 하나를 상환한다
# choice 사용

print() # 줄 바꿈을 위한 코드

dice = [1, 2, 3, 4, 5, 6]
i = 0
while i != 3:
    i = random.choice(dice)
    print(i) # choice는 리스트 안에 무작위 요소 하나를 상환한다
