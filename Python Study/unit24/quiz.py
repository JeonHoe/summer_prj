# 연습문제
path = 'C:\\users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename = x[-1]
print(filename)

print() # 줄 바꿈을 위한 코드

# 참고 raw 문자열 사용하기
# 문자열 앞에 'r' 또는 'R'을 붙이면 raw 문자열이 된다
# 이 raw 문자열은 이스케이프 시퀀스를 그대로 저장할 때 사용한다
# 이는 즉 다음과 같은 '\'를 '\\'로 두 번 쓰지 않고 한 번만 쓰게 만든다.
print(r'C:\users\dojang\AppData\Local\Programs\Python\\Python36-32\python.exe')

print() # 줄 바꿈을 위한 코드

# 심사문제1
s = input()
arr = s.split()
for i in range(len(arr)):
    if arr[i].count('.') or arr[i].count(','):
        arr[i] = arr[i].strip(',.')
print(arr)
the_c = arr.count('the')
print(the_c)

print() # 줄 바꿈을 위한 코드

# 심사문제2
arr = list(map(int, input().split(';')))
arr.sort(reverse=True)
for i in range(len(arr)):
    print('{0:>9,}'.format(arr[i]))
