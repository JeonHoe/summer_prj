# 중첩 루프 사용하기

# 사각형 별 출력
# 5 X 5 사각형
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

print() # 줄 바꿈을 위한 코드

# 모양을 바꿔 3 X 7 사각형
for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

print() # 줄 바꿈을 위한 코드

# 계단식 별 출력하기
for i in range(5):
    for j in range(5):
        if i >= j:
            print('*', end='')
    print()

print() # 줄 바꿈을 위한 코드

# 대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
