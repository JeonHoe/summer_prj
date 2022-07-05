# FizzBuzz 문제

# 논리 연산자의 사용
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('PizzBuzz')
    elif i % 3 == 0:
        print('Pizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print() # 줄 바꿈을 위한 코드

# 논리 연산자 사용하지 않고 공배수 해결
for i in range(1, 101):
    if i % 15 == 0:
        print('PizzBuzz')
    elif i % 3 == 0:
        print('Pizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print() # 줄 바꿈을 위한 코드

# 코드 단축하기
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 단락 평가를 이용한 단축

print() # 줄 바꿈을 위한 코드

# 단락 평가 확인
# True는 1로, False는 0으로 연산되는 점을 이용한 문장 출력
print('sentence' * True) # print('sentence' * 1)과 동일하다
print('sentence' * False) # print('sentence' * 0)으로 공백이 출력된다
# 단락 평가로 보는 or 구문의 활용
i = 0
print('sentence' or i) 
# 'sentence'라는 문자열은 True이므로 단락 평가의 특징 상 'sentence'가 그대로 출력된다
print('' or i)
# 공백 문자열은 False이므로 단락 평가 상 두 번째 값인 변수 i에 따라 결과가 출력된다
# 따라서 변수 i의 값이 출력된다
