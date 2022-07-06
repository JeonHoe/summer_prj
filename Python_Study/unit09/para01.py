# 여러 줄로 된 문자열 사용하기
hello = """Hello, World!
안녕하세요.
Python입니다."""

print(hello) # '''이나 """로 여러 줄에 문자열을 사용할 수 있다

print() # 줄 바꿈을 위한 코드

# 문자열 안에 작은따옴표나 큰따옴표 포함하기
s = "python isn't difficult"
print(s) # 작은따옴표가 포함된 문자를 사용할 때 문자열을 큰따옴표로 묶어준다
s = 'He said "Python is easy"'
print(s) # 큰따옴표가 포함된 문자를 사용할 때 문자열을 작은따옴표로 묶어준다
# 하지만 작은따옴표 안에서는 작은따옴표를 포함한 문자열을 사용할 수 없고, 
# 반대로 큰따옴표 안에서는 큰따옴표를 포함한 문자열을 사용할 수 없다
# 예를 들어 'python isn't difficult'을 print로 출력하면 구문 에러가 발생한다
# 이러한 경우 제어문자 '\''과 '\"'을 사용하여 문자열을 사용한다.
s = 'python isn\'t difficult'
print(s)
