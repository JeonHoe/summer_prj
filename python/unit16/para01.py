# 참고 : for반복문의 변수 i를 변경할 수 있는지에 대하여
for i in range(10):
    print(i, end=' ')
# 결과 --> 0 1 2 3 ... 8 9
print() # 줄 바꿈을 위한 코드
for i in range(10):
    print(i, end=' ')
    i = 10
# 결과 --> 0 1 2 3 ... 8 9
# 출력창에 반복문에 할당한 i가 나온 후 i는 10이 된다
# 하지만 다시 반복문이 시작할 때 i는 다음 반복값으로 덮어써진다
# 따라서 값을 할당해도 i는 영향을 받지 못한다

print('\n') # 줄 바꿈을 위한 코드

# 시퀀스 객체로 반복하기
# 1. 리스트
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)
# 2. 튜플
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)
# 3. 문자열
for letter in 'Python':
    print(letter, end=' ')
print() # 줄 바꿈을 위한 코드
# 문자열 뒤집어서 출력하기
for letter in reversed('Python'):
    print(letter, end=' ')
