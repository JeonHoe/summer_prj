# 빈 딕셔너리 만들기
x = {}; print(x)
y = dict(); print(y)

print() # 줄 바꿈을 위한 코드

# dict로 딕셔너리 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72) # '키'='값' 형식
print(lux1)
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72])) # zip으로 키 리스트와 값 리스트를 묶음
print(lux2)
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)]) # ('키', '값') 형태의 튜플 형식
print(lux3)
lux4 = dict({'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}) # 중괄호로 딕셔너리를 만듦
print(lux4)

print() # 줄 바꿈을 위한 코드

# 딕셔너리 키에 접근하고 값 할당하기
# 키 접근
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(lux['health'])
# 값 할당
lux['health'] = 2037
print(lux)
# 새로운 키 추가, 값 할당하기
lux['mana_regen'] = 3.28
print(lux)
# 없는 키를 가져오라고 할 경우 에러창이 뜬다

print() # 줄 바꿈을 위한 코드

# 딕셔너리 안에 키가 있는지 확인하기
# 키 in 딕셔너리
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print('health' in lux)
print('attack_speed' in lux)
# 키가 없는지를 확인할 경우에는 'not in' 사용
print('attack_speed' not in lux)
print('health' not in lux)

print() # 줄 바꿈을 위한 코드

# 딕셔너리 키의 개수 구하기
# len(딕셔너리)
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
print(len(lux))
