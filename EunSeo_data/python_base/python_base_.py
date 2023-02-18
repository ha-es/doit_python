# 자료구조의 변경
# menu = {"커피","우유","쥬스"}
# print(menu, type(menu))


# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

#<-------------------------------------------------->#
# Quiz
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
# 추첨 프로그램 작성하기

# 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨, 중복 불가
# 조건 3 : readom 모듈의 shuffle 과 sample 활용



from random import *
# users = [ 1, 2, 3, 4, 5, 6,7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

users = range(1,21)  # 1부터 20까지 숫자 생성
#print(type(users))   #type이 range이기 때문에 list로 바꿔야함
users = list(users)
#print(type(users))

shuffle(users)

print("-- 당첨자 발표 --")
print("치킨 당첨자" , sample(users,1))
print("커피 당첨자" , sample(users, 3),"\n")
# 이렇게 되면 중복이 발생할 수 있음

winners = sample(users, 4)  #아예 4명을 뽑고 진행하기
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))

