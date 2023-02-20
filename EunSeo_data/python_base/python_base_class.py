# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"   # 유닛의 이름
# hp = 40         # 유닛의 체력
# damage = 5      # 유닛의 공격력

# print("{}유닛이 생성되었습니다.".format(name))
# print("체력은 {0}, 공격력은 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"   
# tank_hp = 150     
# tank_damage = 35      

# print("{}유닛이 생성되었습니다.".format(tank_name))
# print("체력은 {0}, 공격력은 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"   
# tank2_hp = 150     
# tank2_damage = 35  



# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [ 공격력 {2} ]"\
#         .format(name, location, damage))
    


# attack(name, "1시" , damage)
# attack(tank_name, "1시" , tank_damage)
# attack(tank2_name, "1시" , tank2_damage)


# 클래스 -> 붕어빵 틀
# 틀은 한 개, 붕어빵은 무한정!

class Unit:
    def __init__(self, name, hp, damage) :      # 기본 __init__
        self.name = name    # 멤버변수
        self.hp=hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력은 {0}, 공격력은 {1}\n".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크",150, 35)


#<------------------------------------------------------------->
# __init__
# 객체가 생성될 때, self를 제외한 동일한 개수만큼 인스턴스를 써야함


#<------------------------------------------------------------->
# 멤버 변수
# 클래스 내에서 정의된 변수

# 멤버 변수 외부에서 사용 가능
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))


# 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 =Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True     # 클래스외부에서 변수 추가 가능, 기존에 있는 다른 변수에는 적용 불가

if wraith2.clocking ==True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))