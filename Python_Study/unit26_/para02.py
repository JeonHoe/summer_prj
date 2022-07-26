# 세트에 요소 추가하기
a = {1,2,3,4}
a.add(5)
print(a)

# 세트에 특정 요소 삭제하기
a.remove(3)
print(a) # remove는 세트 안에 특정 요소가 없으면 에러 출력
a.discard(2)
print(a) # discard는 세트 안에 특정 요소가 없으면 그냥 넘어간다

print()

# 세트에서 임의의 요소 삭제
a = {1, 2, 3, 4}
print(a.pop()) # 세트 내에서 임의의 요소를 빼서 반환
print(a)

print()

# 세트의 모든 요소 삭제
a = {1, 2, 3, 4}
a.clear()
print(a)

print()

# 세트의 요소 개수 구하기
a = {1, 2, 3, 4}
print(len(a))
