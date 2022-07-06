# 리스트 할당과 복사
a = [0, 0, 0, 0, 0]
b = a # 선언된 리스트 b와 리스트 a가 같은 메모리 주소를 사용한다
print(a is b) # 이는 리스트 a와 리스트 b는 같은 객체임을 의미한다
# 따라서 리스트 b를 변화하면 리스트 a 역시 같이 변한다
b[2] = 99
print(b)
print(a)
# 리스트 a와 리스트 b를 완전히 두 개로 만들려면 copy 메서드를 사용한다
a = [0, 0, 0, 0, 0]
b = a.copy()
print(a is b) # 둘이 서로 다른 객체임을 알 수 있다
b[2] = 99
print(b)
print(a)

print() # 줄 바꿈을 위한 코드

# 인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value) # enumerate을 사용하면 인덱스와 요소를 함께 꺼내올 수 있다
# 인덱스가 0부터 출력되는 것이 마음에 들지 않아 1부터 출력하고 싶다면 다음과 같이 사용한다
print() # 줄 바꿈을 위한 코드
for index, value in enumerate(a, start=1):
    print(index, value)

print() # 줄 바꿈을 위한 코드

# 리스트의 가장 큰 수, 가장 작은 수, 합계 구하기
# 가장 작은 수
# 방법1
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)
# 방법2
a.sort()
print(a[0])
# 방법3
print(min(a))

print() # 줄 바꿈을 위한 코드

# 가장 큰 수
# 방법1
a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)
# 방법2
a.sort(reverse=True)
print(a[0])
# 방법3
print(max(a))

print() # 줄 바꿈을 위한 코드

# 합계 구하기
a = [38, 21, 53, 62, 19]
print(sum(a))

print() # 줄 바꿈을 위한 코드

# 리스트 표현식
a = [i for i in range(10)]
b = list(i for i in range(10))
print(a)
print(b)

# 응용
a = [i + 5 for i in range(10)]
print(a)

# if 조건식 추가
a = [i for i in range(10) if i % 2 == 0]
print(a)

# for 반복문과 if 조건문 여러 개 사용
a = [i * j for i in range(2, 10)
           for j in range(1, 10)]
print(a)

print() # 줄 바꿈을 위한 코드

# 리스트에 map 사용하기
a = [1.2, 2.5, 3.7, 4.6]
print(list(map(int, a)))
