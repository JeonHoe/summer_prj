# 빈 리스트 만들기
a = []; print(a)
b = list(); print(b)

print() # 줄 바꿈을 위한 코드

# range를 사용하여 리스트 만들기
print(range(10))
print(range(0, 10))
# 둘 다 같은 내용을 담기 때문에 같은 결과값이 나온다
# 하지만 리스트가 아니므로 0부터 9가 아닌 'range(0, 10)'이 출력된다
a = list(range(10)); print(a)
b = list(range(5, 12)); print(b)
c = list(range(-4, 10, 2)); print(c)
d = list(range(10, 0, -1)); print(d)