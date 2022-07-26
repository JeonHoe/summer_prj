# 가변 인수 함수

# 인수의 개수가 정해지지 않은 가변 인수에 사용
# 매개변수 앞에 '*'를 붙여서 만듬

def print_n(*args):
    for i in args:
        print(i)

print_n(10)
print_n(10, 20, 30, 40)

print()

# 키워드 인수 사용

def personal_info(name, age, address):
    print('이름 :', name)
    print('나이 :', age)
    print('주소 :', address)

personal_info('홍길동', 30, '서울시 용산구 이촌동')
personal_info(age = 30, address= '서울시 용산구 이촌동' , name = '임꺽정')

print()

# 키워드 인수와 딕셔너리 언패킹 사용

x = {'name' : '홍길동', 'age' : 30, 'address' : '서울시 용산구 이촌동'}
personal_info(**x)

print()

# '*'이 아닌 '**'을 쓰는 이유

personal_info(*x)
# 딕셔너리에 경우 '*'를 사용하여 한 번 언패킹하면 키만 출력된다
# 키가 아닌 값을 언패킹하기 위해서 딕셔너리는 두 번 언패킹한다

print()

# 키워드 인수를 사용하는 가변 인수 함수 만들기

def p_info(**kwargs):
    for kw, args in kwargs.items():
        print(kw, ' : ', args, sep='')

p_info(name='홍길동')
x = {'name' : '홍길동'}
p_info(**x)
p_info(name='장길산', age=20, address='서울시 용산구 이촌동')
y = {'name' : '장길산', 'age' : 20, 'address' : '서울시 용산구 이촌동'}
p_info(**y)

