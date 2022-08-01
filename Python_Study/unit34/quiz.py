# 연습문제 : 게임 캐릭터 클래스 만들기
from re import A


class Knight():
    def __init__(self, **kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.armor = kwargs['armor']
    
    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

print()

# 심사문제 : 게임 캐릭터 클래스 만들기
class Annie():
    def __init__(self, **kwrgs):
        self.health = kwrgs['health']
        self.mana = kwrgs['mana']
        self.ability_power = kwrgs['ability_power']
    
    def tibbers(self):
        res = self.ability_power * 0.65 + 400
        print("티버 : 피해량", res)

health, mana, ability_power = map(float, input().split())

x = Annie(health= health, mana= mana, ability_power= ability_power)
x.tibbers()

