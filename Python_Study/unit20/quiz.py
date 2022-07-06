# 연습문제
for i in range(1, 101):
    if i % 22 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)

print() # 줄 바꿈을 위한 코드

# 심사문제
a, b = map(int, input().split())
for i in range(a, b+1):
    if i % 35 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
        