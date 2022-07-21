# 딕셔너리 조작하기

# 딕셔너리 키-값 추가하기

# setdefault : 키-값 쌍 추가
# update : 키의 값 수정, 키가 없으면 키-값 쌍 추가

# 딕셔너리에 키와 기본값 저장하기
# setdefault(키)는 딕셔너리에 키-값 쌍을 추가한다. 키만 지정하면 값에 None을 저장
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.setdefault('e')
print(x)
# setdefault(키, 값)은 딕셔너리에 키-값 쌍을 추가한다
x.setdefault('f', 100)
print(x)

print() # 줄 바꿈을 위한 코드

# 딕셔너리에서 키의 값 수정하기
# update(키=값)은 이름 그대로 딕셔너리에서 키의 값을 수정한다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.update(a=90) # 딕셔너리에 있던 키 a에 값 변화
print(x)
x.update(e=50) # 만약 딕셔너리에 없으면 키-값 쌍을 추가한다
print(x)
x.update(a=900, f= 60) # 컴마를 이용해 한 번에 여러 작업 수행 가능
print(x)

print() # 줄 바꿈을 위한 코드

# update(키=값)은 키가 문자열일 때만 사용 가능
# 만약 키가 숫자일 경우, update(딕셔너리)로 딕셔너리를 넣어 값을 수정한다
y = {1 : 'one', 2 : 'two'}
y.update({1 : 'ONE', 3 : 'THREE'})
print(y)

# 딕셔너리가 아닌 리스트와 튜플로도 수정 가능
# 리스트는 [[키1, 값1], [키2, 값2]] 형식으로 키와 값을 리스트로 만들고 이 리스트를 다시 리스트 아넹 넣어서 키-값 쌍을 나열
# 튜플 역시 같은 형식 ((키1, 값1), (키2, 값2))
y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

# update(반복가능한객체)는 키-값 쌍으로 된 반복 가능한 객체로 값을 수정
# 즉, 다음과 같이 키 리스트와 값 리스트를 묶은 zip 객체로 수정
y.update(zip([1, 2],['one', 'two']))
print(y)

# 참고 : setdefault와 update의 차이
# setdefault는 키-값 쌍을 추가할 수 있으나 이미 들어있는 키의 값은 수정할 수 없다
# 반면 update는 키-값을 쌍을 추가할 수 있으며 이미 들어있는 키의 값을 수정할 수 있다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.setdefault('a', 90)
print(x)

print() # 줄 바꿈을 위한 코드

# 딕셔너리에서 키-값 쌍 삭제하기
#pop(키)는 딕셔너리에서 특정 키-값 쌍을 삭제한 뒤 삭제한 값을 반환한다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(x.pop('a')) # 삭제한 키에 값이 반환된다
print(x) # 특정 키-값 삭제 이후의 딕셔너리가 출력된다
# pop(키, 기본값)은 딕셔너리 안에 특정 키가 없을 경우 지정한 기본값을 출력
print(x.pop('z', 0)) # 딕셔너리 x 안에 키 z는 없다, 옆에 0은 없을 경우 기본값 0을 출력한다는 의미

# del로도 특정 키-값 쌍을 삭제할 수 있다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
del x['a']
print(x)
#del x['z']
#print(x)   # 하지만 딕셔너리 안에 없는 키의 값은 삭제할 수 없으며 실행 시 에러가 출력

print() # 줄 바꿈을 위한 코드

# 딕셔너리 모든 키-값 쌍 삭제하기
# clear() 메서드는 딕셔너리 안에 모든 키-값 쌍을 삭제한다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.clear()
print(x) # 빈 딕셔너리 {}가 출력된다

print() # 줄 바꿈을 위한 코드

# 딕셔너리에서 키의 값을 가져오기
# get('키')는 딕셔너리 안에 '키'의 값을 반환하는 메서드이다
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(x.get('a'))
# get('키', '기본값')처럼 기본값을 지정하면 딕셔너리 안에 키가 없을 경우 기본값이 반환된다
print(x.get('z', 1))

print() # 줄 바꿈을 위한 코드

# 딕셔너리에서 키-값 쌍 모두 가져오기
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(x)
# 키-값 쌍 모두 가져오기 - items
print(x.items())
# 키를 모두 가져오기 - keys
print(x.keys())
# 값을 모두 가져오기 - values
print(x.values())

print() # 줄 바꿈을 위한 코드

# 리스트와 튜플로 딕셔너리 만들기
# 키 리스트
keys = ['a', 'b', 'c', 'd']
# 키 리스트를 이용한 딕셔너리 생성
x = dict.fromkeys(keys)
print(x) # 값은 입력되지 않았으므로 당연히 값은 빈 딕셔너리가 생성된다
# dict.fromkeys('키 리스트', '값')처럼 키 리스트와 값을 지정하면 해당 값이 키의 값으로 지정
x = dict.fromkeys(keys, 100) 
print(x)

print() # 줄 바꿈을 위한 코드

# 참고 : defaultdict 사용
# 지금까지 사용한 딕셔너리는 없는 키에 접근할 경우 에러가 발생
# 에러가 발생하지 않게 하기 위해 defaultdict 사용
# defaultdict는 키가 없어도 에러가 발생하지 않고 기본값이 반환
# defaultdict는 collections 모듈에 포함
# 형태 : defaultdict('기본값생성함수')

from collections import defaultdict
y = defaultdict(int) # int로 기본값 생성
print(y['z'])
print(int()) # int()은 아무것도 입력받지 않았을 때 기본값으로 0 반환
z = defaultdict(lambda : 'python')
print(z['a'])
print(z[0])
