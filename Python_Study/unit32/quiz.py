# 연습문제 : 이미지 파일만 가져오기
from lib2to3.pgen2 import pgen


files = ['font', '1.png', '10.jpg', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('jpg') != -1 or x.find('png') != -1, files)))

# 심사문제 : 파일 이름을 한꺼번에 바꾸기
files = input().split()
print(list(map(lambda x : (x.split('.')[0]).zfill(3) + '.' + x.split('.')[1] if len(str.split('.')[0]) < 3 else x, files)))