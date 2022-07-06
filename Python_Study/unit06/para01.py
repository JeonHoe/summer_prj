# 변수 여러 개를 한 번에 만들기
# 상황1 : 각 변수에 다른 값을 선언할 때
x, y, z = 10, 20, 30
print(x); print(y); print(z)
# 변수의 개수와 값의 개수가 같지 않으면 출력창에 에러가 뜬다

print() # 줄 바꿈을 위한 코드

# 상황2 : 여러 변수에 같은 값을 선언할 때
x = y = z = 10
print(x); print(y); print(z)

print() # 줄 바꿈을 위한 코드

# 상황3 : 두 변수에 값을 서로 바꿀 때 (swap)
x, y = 10, 20
print(x); print(y)
x, y = y, x
print(x); print(y)

print() # 줄 바꿈을 위한 코드

# 빈 변수 만들기
x = None
print(x) # None이 출력되나 None은 아무것도 없다는 것을 의미

print() # 줄 바꿈을 위한 코드

# 변수 삭제하기
x = 10
del x
print(x)
# 변수가 정의되지 않았다는 내용에 에러가 출력창에 뜬다
