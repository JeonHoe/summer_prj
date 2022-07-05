# 연습문제
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxftrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

print() # 줄 바꿈을 위한 코드

# 심사문제
start, stop = map(int, input().split())
a = [2 ** i for i in range(start, stop + 1)]
del a[1]; del a[-2]
print(a)
