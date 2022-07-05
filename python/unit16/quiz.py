# 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i * 10, end=' ')

print('\n') # 줄 바꿈을 위한 코드

# 심사문제
n = int(input())
for i in range(1, 10):
    print('%d * %d = %d' % (n, i, n * i))
