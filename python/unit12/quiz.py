# 연습문제
camille = {
    'health' : 575.6,
    'health_regen' : 1.7,
    'mana' : 338.8,
    'mana_regen' : 1.63,
    'melee' : 125,
    'attack_damage' : 60,
    'attack_speed' : 0.625,
    'armor' : 26,
    'magic_resistance' : 32.1,
    'movement_speed' : 340
}
print(camille['health'])
print(camille['movement_speed'])

print() # 줄 바꿈을 위한 코드

# 심사문제
karr = input().split()
varr = map(float, (input().split()))
d = dict(zip(karr, varr))
print(d)