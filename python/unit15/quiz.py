# 연습문제
x = int(input())
if 10 < x <= 20:
    print('11~20')
elif 20 < x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

print() # 줄 바꿈을 위한 코드

# 심사문제
current_c = 9000
price = 0
age = int(input())
if 7 <= age <=12:
    price = 650
elif 13 <= age <= 18:
    price = 1050
else:
    price = 1250
current_c -= price
print(current_c)
