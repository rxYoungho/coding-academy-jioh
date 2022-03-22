
# def character1():
#     name = "타락파워전사"
#     STR = 4
#     DEX = 4
#     INT = 4
#     LUK = 4
#     gender = "남자"
#     hair = "남자 더벅 머리"
#     weapon = "검"

# def character2():
#     name = "아시안느"
#     STR = 4
#     DEX = 7
#     INT = 4
#     LUK = 4
#     gender = "여자"
#     hair = "여자 더벅 머리"
#     weapon = "몽둥이"

# 클래스 선언!
class Character:
    def __init__(self, name, gender, hair, weapon):
        self.name = name
        self.gender = gender
        self.hair = hair
        self.weapon = weapon
        self.STR = 4
        self.DEX = 4
        self.INT = 4
        self.LUK = 4
    def createCharacter(self):
        print(self.name + "님 환영합니다. 캐릭터 생성이 완료 되었습니다.")

    def getGender(self):
        print(self.name +"의 성별은 "+self.gender+"입니다.")
    
    def getStat(self):
        print(self.STR, self.DEX, self.INT, self.LUK)
    

# 객체 생성!
tarakPowerJunsa = Character("tarakPowerJunsa", "남자", "더벅머리", "검")
asaiane = Character("asaiane", "여자", "더벅머리", "몽둥이")
ziZonPower = Character("ziZonPower", "남자", "더벅머리", "검")
bezzy = Character("bezzy", "중성", "빡빡이", "검")

tarakPowerJunsa.getGender()
bezzy.getStat()
bezzy.createCharacter()

if __name__ == "__main__":
    print("메이플스토리를 시작합니다.")