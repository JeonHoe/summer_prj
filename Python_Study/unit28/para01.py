# N-gram
# N-gram은 문자열에서 N개의 연속된 요소를 추출하는 방법

# 반복문으로 추출하기
text = 'Hello'
for i in range(len(text)-1):
    print(text[i], text[i+1], sep='')

print()

# zip으로 만들기
print(list(zip(text, text[1:])))
two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')

print()

# zip과 리스트 표현식으로 N-gram 만들기
text = 'hello'
print([text[i:] for i in range(3)])
print(list(zip(['hello', 'ello', 'llo']))) # zip 안에 내용물이 하나의 리스트이므로 zip은 자신이 하나의 매개변수를 받았다 여김
print(list(zip('hello', 'ello', 'llo'))) # 컴마로 나눠 3개의 내용물로 받아야 원하는 N-gram이 출력
print(list(zip(*['hello', 'ello', 'llo']))) # 리스트 앞에 *을 붙여주면 리스트 안에 요소를 컴마 단위로 구분할 수 있다
