# 연습문제
i = 0
while True: 
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1

print('\n') # 줄 바꿈을 위한 코드

# 심사문제
start, stop = map(int, input().split())
i = start
while True:
    if i > stop:
        break
    if i % 10 == 3:
        i += 1
        continue
    print(i, end=' ')
    i += 1
