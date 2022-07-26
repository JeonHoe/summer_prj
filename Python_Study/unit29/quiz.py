# 연습문제
x = 10
y = 3

def get_quotient_remainder(x, y):
    q = x // y
    r = x % y
    return q, r

quotient, remainder = get_quotient_remainder(x, y)
print('몫 : {0}, 나머지 : {1}'.format(quotient, remainder))

# 심사문제
x, y = map(int, input().split())

def calc(x, y):
    return x + y, x - y, x * y, x / y

a, s, m, d = calc(x, y)
print('덧셈 : {0}, 뺄셈 : {1}, 곱셈 : {2}, 나눗셈 : {3}'.format(a, s, m, d))
