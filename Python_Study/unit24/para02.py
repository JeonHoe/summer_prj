# 문자열 왼쪽 정렬하기
print('python'.ljust(10)) # python의 길이를 10으로 만든 뒤 왼쪽으로 정렬, 남는 공간은 공백

# 문자열 오른쪽 정렬하기
print('python'.rjust(10)) # python의 길이를 10으로 만든 뒤 왼쪽으로 정렬, 남는 공간은 공백

# 문자열 가운데 정렬하기
print('python'.center(10)) # python의 길이를 10으로 만든 뒤 왼쪽으로 정렬, 남는 공간은 공백

print() # 줄 바꿈을 위한 코드

# 메서드 체이닝
# 문지열 메서드는 처리한 결과를 반환하도록 만들어져 있다
# 따라서 메서드를 계속 연결해 호출하는 메서드 체이닝 가능
print('python'.rjust(10).upper())

print() # 줄 바꿈을 위한 코드

# 문자열 왼쪽에 0 채우기
print('35'.zfill(4)) # 지정된 길이에 맞게 숫자 앞에 0을 채움
print('3505'.zfill(3)) # 지정된 길이가 짧다면 아무것도 채우지 않음
print('3.5'.zfill(6))
print('hello'.zfill(10)) # 문자열 앞에도 사용 가능

print() # 줄 바꿈을 위한 코드

# 문자열 위치 찾기
# find
print('apple'.find('pl')) # 'pl'이 발견된 인덱스를 출력
print('apple'.find('xy')) # 문자열 안에 찾고자 하는 특정 문자열이 없다면 -1 출력
print('apple pineapple'.find('pl')) # 특정 문자열이 여러 개일 경우 처음 찾은 인덱스 출력
# index
print('apple'.index('pl')) # 'pl'이 발견된 인덱스를 출력
# print('apple'.find('xy')) # 단 문자열 안에 찾고자 하는 특정 문자열 부재 시 에러 출력
print('apple pineapple'.index('pl')) # 특정 문자열이 여러 개일 경우 처음 찾은 인덱스 출력

print() # 줄 바꿈을 위한 코드

# 오른쪽에서부터 문자열 위치 찾기
# find
print('apple pineapple'.rfind('pl')) # 특정 문자열이 여러 개일 경우 처음 찾은 인덱스 출력
print('apple pineapple'.rfind('xy')) # 문자열 안에 찾고자 하는 특정 문자열이 없다면 -1 출력
# index
print('apple pineapple'.rindex('pl')) # 특정 문자열이 여러 개일 경우 처음 찾은 인덱스 출력
# print('apple pineapple'.rindex('xy')) # 단 문자열 안에 찾고자 하는 특정 문자열 부재 시 에러 출력

print() # 줄 바꿈을 위한 코드

# 문자열 개수 세기
print('apple pineapple'.count('pl')) # 특정 문자열의 개수를 반환한다
print('apple pineapple'.count('xy'))
