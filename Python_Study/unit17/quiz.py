# 연습문제
i = 2
j = 5

while i < 33 and j > 0:
    print(i, j)
    i *= 2
    j -= 1

print() # 줄 바꿈을 위한 코드

# 심사문제
price = 1350
cash = int(input())
cash -= price
while cash >= 0:
    print(cash)
    cash -= price
    