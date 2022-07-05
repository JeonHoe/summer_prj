# 연습문제
x = 5
if x != 10:
    print('ok')

print() # 줄 바꿈을 위한 코드

# 심사문제
price = int(input())
coupon = input()
if coupon == 'Cash3000':
    coupon = -3000
if coupon == 'Cash5000':
    coupon = -5000
print(price+coupon)