# 튜플
# 리스트와 다르게 내용 변경, 추가를 할 수 없음
# 속도가 리스트보다 빨라서 변경되지 않는 값들을 사용할 때 좋음
menu = ("돈까스", "치즈까스")
print(menu[0])

# 새롭게 추가 불가
# menu.add("생선까스")

# name = "원우"
# age = 28
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = ("원우", 28, "코딩")
print(name, age, hobby)