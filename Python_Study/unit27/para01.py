# 파이썬 객체를 파일에 저장하기, 가져오기
# 파이썬 객체를 파일에 저장하는 과정을 피클링(pickling)
# 반대로 파일에서 객체를 가져오는 과정을 언피클링(inpickling)이라고 한다

# 파이썬 객체 파일에 저장
from audioop import add
import pickle

name = 'James'
age = 17
address = '서울시 서초구 반포동'
score = {'Korean' : 90, 'english' : 95, 'math' : 85, 'science' : 82}

with open('james.p', 'wb') as file: # picke을 알리는 확장자명 '.p', 바이너리 쓰기 사용(wb)
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(score, file)

# 파일에서 파이썬 객체 읽기

with open('james.p', 'rb') as file:
    name1 = pickle.load(file)
    age1 = pickle.load(file)
    address1 = pickle.load(file)
    score1 = pickle.load(file)
print(name1)
print(age1)
print(address1)
print(score1)

