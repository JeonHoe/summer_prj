# 서식 지정자로 문자열 넣기
print('I am %s' % 'James')
name = 'Maria'
print('I am %s' % name)

print() # 줄 바꿈을 위한 코드

# 서식 지정자로 숫자 넣기
print('I am %d years old' % 20)

# 서식 지정자로 소수점 표현하기
print('%f' % 2.3)
print('%.2f' % 2.3) # '%.자릿수f % 숫자'는 소수점의 자리에 맞게 실수를 표현한다

print() # 줄 바꿈을 위한 코드

# 서식 지정자로 문자열 정렬하기
print('%10s' % 'python') # '%길이 % 문자열'은 문자열을 지정된 길이로 바꾼 뒤 오른쪽 정렬시킨다
# 오른쪽 정렬이 아닌 왼쪽 정렬시키기
print('%-10s' % 'python') # '%-길이 % 문자열'은 문자열을 지정된 길이로 바꾼 뒤 왼쪽 정렬시킨다


print() # 줄 바꿈을 위한 코드

# 자릿수가 다른 숫자 출력하기
# 정수
print('%10d' % 15); print('%10d' % 1000)
# 실수
print('%10.2f' % 2.3); print('%10.2f' % 2000.3)

print() # 줄 바꿈을 위한 코드

# 서식 지정자로 문자열 안에 값 여러 개 넣기
print('Today is %d %s.' % (3, 'April')) # 띄워쓰기를 잘해줘야 원하는 형식대로 출력된다

# format 메서드 사용하기
print('Hello, {0}'.format('world!')) # '{인덱스}.format(값)' 형식으로 문자열 인덱스에 맞는 값을 문자열에 넣는다
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)) # 여러 개도 넣는 게 가능
print('{0} {0} {1} {1}'.format('Python', 'Script')) # 같은 값을 여러 개 넣는 것도 가능
print('Hello, {} {} {}'.format('Python', 'Script', 3.6)) # 인덱스를 생략하면 format에 지정된 순서대로 값이 들어간다
print('Hello, {language} {version}'.format(language='Python', version=3.6)) # 인덱스가 아닌 이름으로 지정해도 된다

print() # 줄 바꿈을 위한 코드

# 문자열 포매팅에 변수를 그대로 사용하기
language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')

print() # 줄 바꿈을 위한 코드

# 중괄호 출력
print('{{ {0} }}'.format('Python')) # format을 사용할 때 중괄호를 출력하고 싶으면 '{{', '}}'를 사용한다

print() # 줄 바꿈을 위한 코드

# format 메서드로 문자열 정렬
print('{0:<10}'.format('Python'))
print('{0:>10}'.format('Python')) 
# 숫자로 길이를 지정하고 부등호의 방향에 따라 정렬 위치가 정해진다

print() # 줄 바꿈을 위한 코드

# 숫자 개수 맞추기
# 정수
print('%03d' % 1)
print('{0:03d}'.format(35))

# 실수
print('%08.2f' % 3.6)
print('{0:08.2f}'.format(151.37))

print() # 줄 바꿈을 위한 코드

# 채우기와 정렬을 조합해서 사용하기
# '{인덱스:[채우기][정렬][길이].[자릿수][자료형]}'
print('{0:0<10}'.format(15)) # 길이 10, 왼쪽으로 정렬 남은 공간 0으로 채우기
print('{0:0>10}'.format(15)) # 길이 10, 오른쪽으로 정렬 남은 공간 0으로 채우기
print('{0:0>10.2f}'.format(15)) # 길이 10, 오른쪽으로 정렬 소수점 자릿수는 2, 남는 공간 0으로 채우기
print('{0: >10}'.format(15)) # 길이 10, 오른쪽으로 정렬 남은 공간 공백으로 채우기
print('{0:>10}'.format(15)) # 채우기 부분에 아무것도 없어도 남은 공간은 공백으로 채운다
print('{0:x>10}'.format(15)) # 길이 10, 오른쪽으로 정렬 남은 공간 'x'으로 채우기

print() # 줄 바꿈을 위한 코드

# 금액에서 천단위로 콤마 넣기
print(format(1493500, ','))
print('%20s' % format(1493500, ',')) # 길이 20, 오른쪽으로 정렬
print('{0:,}'.format(1493500))
print('{0:>20,}'.format(1493500)) # 길이 20, 오른쪽 정렬
print('{0:0>20,}'.format(1493500)) # 길이 20, 오른쪽 정렬, 남는 공간 0으로 채우기
