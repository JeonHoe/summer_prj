# 반복문으로 딕셔너리의 키-값 쌍 모두 출력하기
# for i in '딕셔너리':의 경우 i에 딕셔너리 안에 키 입력된다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
for i in x:
    print(i, end=' ')

print('\n') # 줄 바꿈을 위한 코드

# for '키', '값' in 딕셔너리.items():의 경우 '키'와 '값'에 딕셔너리 안에 키와 값이 입력된다
for keys, values in x.items():
    print(keys, ':', values, sep='', end=' ')

print('\n') # 줄 바꿈을 위한 코드

# 딕셔너리의 키만 출력하기
# for i in '딕셔너리':의 경우 i에 딕셔너리 안에 키 입력된다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
for i in x:
    print(i, end=' ')

print('\n') # 줄 바꿈을 위한 코드

# for '키' in '딕셔너리'.keys():의 경우 '키'에 딕셔너리 안에 키가 입력된다
for k in x.keys():
    print(k, end=' ')

print('\n') # 줄 바꿈을 위한 코드

# 딕셔너리의 키만 출력하기
# for '값' in '딕셔너리'.values():의 경우 '값'에 딕셔너리 안에 값이 입력된다
for v in x.values():
    print(v, end=' ')

