# 불과 비교
# 객체 비교
print(1 == 1.0) # '=='을 이용한 두 값에 비교
print(1 is 1.0) # 'is'을 이용한 두 객체에 비교
# 값은 같으나 두 값에 객체는 정수와 실수로 서로 다르다
print(1 is not 1.0)

print() # 줄 바꿈을 위한 코드

# 객체 비교 확인
print(id(1)) # 정수형 객체 1이 저장된 메모리 위치
print(id(1.0)) # 실수형 객체 1.0이 저장된 메모리 위치
# --> 실행 결과 출력창에서 출력된 값이 다름을 확인할 수 있음

print() # 줄 바꿈을 위한 코드

# 정수, 실수, 문자열을 불로 만들기
print(bool(1))
print(bool(0))
print(bool(-125)) 
print(bool(1.5))
print(bool(0.0)) # bool형에 0을 제외한 모든 정수와 실수는 True
print(bool('False'))
print(bool('')) # bool형에 공백을 제외한 모든 문자열은 True

print() # 줄 바꿈을 위한 코드

# 단락 평가
print(False and True)
print(False and False) 
# and 연산자는 첫 번째 값이 거짓이면 두번째 값은 확인하지 않고 False으로 결정
print(True or True)
print(True or False) 
# or 연산자는 첫 번째 값이 참이면 두번째 값은 확인하지 않고 True로 결정
print(True and 'Python')
# and 연산자의 첫번째 값이 True로 두번째 값을 확인해야 함
# 'Python'은 bool형으로 봤을 때 True로 결과값이 True로 예상되나 결과는 'Python'이다
#  이는 파이썬이 논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환하기 때문이다
print('Python' and True)
print('Python' and False)
print(False and 'Python')
print(0 and 'Python') 
# 정수 0은 False로 and 연산자에서 첫번째에 False가 나오면 두번째는 확인하지 않는다
# 이로 인해 결과는 마지막 단락 평가를 한 정수 0이 출력된다
print(True or 'Python')
print('Python' or True)
print(False or 'Python')
print(0 or 'Python')
