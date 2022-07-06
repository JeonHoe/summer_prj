# 연습문제
written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')

print() # 줄 바꿈을 위한 코드

# 심사문제
k, e, m, s = map(int, input().split())
arg = (k + e + m + s) / 4
if 0<=k<=100 and 0<=e<=100 and 0<=m<=100 and 0<=s<=100:
    if arg >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')
    