# 상속

# 일반 유닛
class Unit: 
    def __init__(self, name, hp) :      # 기본 __init__
        self.name = name    # 멤버변수
        self.hp=hp
        
        
# 공격 유닛    
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, damage) :
        Unit.__init__(self, name, hp)  # 상속 받는 클래스 
        self.damage = damage
        
    def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [ 공격력 {2} ]"\
                .format(self.name, location, self.damage))
            
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        
        if self.hp <=0:
            print("{0} : 파괴 되었습니다.".format(self.name))
            
 
 # 의무병 -> 데미지 0
            
# 유닛 만들기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

#<------------------------------------------------------------->
# 다중 상속
# 부모 클래스가 2개 이상

 # 날 수 있는 기능을 가진 클래스
class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1}시 방향으로 날아갑니다. [ 속도 {2} ]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")