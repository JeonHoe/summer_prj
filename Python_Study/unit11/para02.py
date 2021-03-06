# 시퀀스 객체의 요소 개수 구하기 
# 1. 리스트와 튜플
# len으로 리스트와 튜플의 요소 개수를 구할 수 있다
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
b = (38, 76, 43, 62, 19)
print(len(a)); print(len(b))

# 2. range
print(len(range(0, 10, 2)))

# 3. 문자열
hello = 'Hello, world!'
print(len(hello))

# 참고 : 'UTF-8' 문자열의 바이트 수 구하기
hello = '안녕하세요'
print(len(hello.encode('UTF-8')))

print() # 줄 바꿈을 위한 코드

# 인덱스 사용과 '__getitem__' 메서드
a = [38, 21, 53, 62, 19]
print(a[2])             # 인덱스 사용하여 요소 출력
# 양수 인덱스는 맨앞을 시작으로 0에서 시작
print(a.__getitem__(2)) # __getitem__ 메서드로 요소 출력
print(a[-3])            # 음수 인덱스로 요소 출력
# 음수 인덱스는 맨끝을 시작으로 -1에서 시작

print() # 줄 바꿈을 위한 코드

# 요소에 할당하기
# 읽기 전용인 튜플, range, 문자열을 사용 불가능
a = [0, 0, 0, 0, 0]
a[0] = 38; a[1] = 21; a[2] = 53; a[3] = 62; a[4] = 19
print(a)

print() # 줄 바꿈을 위한 코드

# 요소 삭제하기
# 읽기 전용인 튜플, range, 문자열을 사용 불가능
a = [38, 21, 53, 62, 19]
print(a)
del a[2] # 리스트 a 안에 2번 인덱스의 값이 삭제
print(a)
