#  변수의 값 할당을 if, else로 축약하기
from re import X


x = 5
if x == 10:
    y1 = x
else:
    y1 = 0
print(y1)
x = 5
y2 = x if x == 10 else 0
print(y2)

print() # 줄 바꿈을 위한 코드

# if 조건문의 동작 방식 알아보기
if True: 
    print('참')
else:
    print('거짓')
if False:
    print('참')
else:
    print('거짓')
if None: # None은 False 취급을 받아 조건문에 쓰면 작동하지 않는다
    print('참')
else:
    print('거짓')
# 위의 조건들 앞에 not을 붙일 경우
if not True: 
    print('참')
else:
    print('거짓')
if not False:
    print('참')
else:
    print('거짓')
if not None:
    print('참')
else:
    print('거짓')
# not을 붙이면 참은 거짓, 거짓은 참으로 바뀌어 결과가 반대로 변한다

print() # 줄 바꿈을 위한 코드

# 조건식 여러 개 지정하기
x = 12
if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')
if x > 0 and x < 20: # 논리 연산자를 이용하여 조건을 여러 개 지정할 수 있다
    print('20보다 작은 양수입니다.')
if 0 < x < 20:
    print('20보다 작은 양수입니다.')
    