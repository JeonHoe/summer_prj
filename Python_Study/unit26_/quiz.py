# 연습문제 공배수 구하기
a = {x for x in range(1,101) if (x%3 == 0)}
b = {x for x in range(1,101) if (x%5 == 0)}

print(a & b)

# 심사문제 공약수 구하기
x, y = map(int, input().split())
a = {i for i in range(1, x + 1) if (x % i == 0)}
b = {i for i in range(1, y + 1) if (y % i == 0)}

divisor = a&b

result = 0
if type(divisor) == set:
    result = sum(divisor)
print(result)
