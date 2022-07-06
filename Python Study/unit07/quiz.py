# 연습문제
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

print() # 줄 바꿈을 위한 코드

# 심사문제
y, m, d, h, mn, s = map(int, input().split())
print(y, m, d, sep='-', end='T')
print(h, mn, s, sep=':')
