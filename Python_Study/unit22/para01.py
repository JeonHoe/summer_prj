# 리스트 조작

# 리스트 확장
# 1개 요소 추가
a = [100, 200, 300]
a.append(400)
print(a)
print(len(a))

print() # 줄 바꿈을 위한 코드

# 여러 개 추가
a = [100, 200, 300]
a.append([500, 600]) # append로 리스트를 넣을 시 리스트 안에 리스트 형성
print(a)
print(len(a))
a = [100, 200, 300]
a.extend([500, 600]) # extend는 입력 받은 리스트의 요소를 리스트 안에 추가
print(a)
print(len(a))

print() # 줄 바꿈을 위한 코드

# 리스트 특정 인덱스에 요소 추가하기
a = [10, 20, 30]
a.insert(2, 500) # insert(인덱스, 요소) 형식으로 리스트의 특정 인덱스에 요소 추가
print(a)
print(len(a))

print() # 줄 바꿈을 위한 코드

# 특정 인덱스에 여러 요소를 추가할 때
a = [10, 20, 30]
a.insert(1, [500, 600]) # append처럼 insert도 한 개 요소만 추가 가능하다
print(a)
print(len(a))
a = [10, 20, 30]
a[1:1] = [500, 600] # 슬라이스를 활용하여 여러 요소를 특정 인덱스에 추가
print(a)
print(len(a))

print() # 줄 바꿈을 위한 코드

# 리스트 요소 삭제
# 특정 인덱스 요소
# pop 사용
a = [100, 200, 300]
a.pop() # 맨 뒤의 요소 삭제
print(a)

a = [100, 200, 300]
a.pop(1) # 인덱스 1의 요소 삭제
print(a)

# del 사용
a = [100, 200, 300]
del a[2] # 인덱스 2의 요소 삭제
print(a)

# 특정 값을 찾아서 삭제하기
a = [10, 20, 30]
a.remove(20) # remove는 인덱스가 아닌 특정 값을 찾아 삭제한다
print(a)
# 하지만 remove는 같은 값이 여러 개 있을 경우 처음 찾은 값만 삭제한다
a = [10, 20, 30, 20]
a.remove(20)
print(a)

print() # 줄 바꿈을 위한 코드

# 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.index(20))
# index 역시 같은 값이 여러 개일 경우 처음 찾은 값에 인덱스만 상환한다

print() # 줄 바꿈을 위한 코드

# 특정 값 개수 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))

print() # 줄 바꿈을 위한 코드

# 리스트 요소 정렬하기
# sort와 sorted
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a) # sort는 기존의 a 리스트 내에서 정렬하여 리스트를 변경한다
print(a.sort()) # 리스트도 변수도 아닌 코드이므로 공백인 None이 출력된다
b = [10, 20, 30, 15, 20, 40]
print(sorted(b)) # 반면 sorted는 리스트 내에 요소들이 정렬되어진 새로운 리스트를 생성한다

print() # 줄 바꿈을 위한 코드

# 리스트 모든 요소 삭제
a = [10, 20, 30]
a.clear()
print(a)
a = [10, 20, 30]
del a[:]
print(a)
