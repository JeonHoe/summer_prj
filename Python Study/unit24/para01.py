# 문자열 조작하기
print('Hello, world!'.replace('world','Python'))
s = 'Hello, world!'
s = s.replace('world', 'Python')
print(s)

print() # 줄 바꿈을 위한 코드

# 문자 바꾸기
# translate와 str.maketrans 
# str.maketrans를 이용해 '바꿀문자' '새문자'의 변환 테이블 생성
table = str.maketrans('aeiou', '12345') # a->1, e->2, i->3, o->4, u->5로 변환시키는 테이블
print('apple'.translate(table)) # 만들어진 테이블을 translate 안에 입력해 문자 변환

print() # 줄 바꿈을 위한 코드

# 문자열 분리하기
# 이제까지 input과 함께 써온 split으로 문자열 분리
print('apple pear grape pineapple orange'.split())

print() # 줄 바꿈을 위한 코드

# 구분자 문자열과 문자열 리스트 연결하기
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])) # 각 요소 사이에 공백으로 연결된 문자열 생성
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])) # 각 요소 사이에 '-'로 연결된 문자열 생성

print() # 줄 바꿈을 위한 코드

# 소문자를 대문자로 바꾸기
print('python'.upper())

# 대문자를 소문자로 바꾸기
print('PYTHON'.lower())

print() # 줄 바꿈을 위한 코드

# 왼쪽 공백 삭제하기
print('  python  '.lstrip())

# 오른쪽 공백 삭제하기
print('  python  '.rstrip())

# 양쪽 공백 삭제하기
print('  python  '.strip())

print() # 줄 바꿈을 위한 코드

# 왼쪽의 특정 문자 삭제하기
print(', python.'.lstrip(',.'))

# 오른쪽의 특정 문자 삭제하기
print(', python.'.rstrip(',.'))

# 양쪽의 특정 문자 삭제하기
print(', python.'.strip(',.'))

print() # 줄 바꿈을 위한 코드

# 구두점을 간단하게 삭제하기
# string 모듈의 punctuation에는 모든 구두점이 들어있다.
import string
print(string.punctuation)
# 따라서  strip 메서드에 string.punctuation를 입력하면
# 문자열 양쪽에 있는 모든 구두점을 삭제할 수 있다
print(', python.'.strip(string.punctuation))
# 공백까지 삭제하고 싶을 경우
print(',python.'.strip(string.punctuation+' '))
