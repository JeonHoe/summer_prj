# 연습문제
for i in range(5):
    for j in range(5):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print() # 줄 바꿈을 위한 코드

# 심사문제
n = int(input())
for i in range(n):
    for j in range(n+i+1):
        if j < n-i:
            print(' ', end='')
        else:
            print('*', end='')
    print()
       