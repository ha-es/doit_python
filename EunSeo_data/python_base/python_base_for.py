# 반복문
# for
# for i in [0, 1, 2, 3, 4] :
#     print("대기번호 : {0}".format(i))
    

# for i in range(1,6) :
#     print("대기번호 : {0}".format(i))


# cafe = ["원우", "민규", "승관"]
# for customer in cafe:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))


#<------------------------------------------------------------->
# while
# customer = "원우"
# index = 5
# while index >=1 :
#     print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -=1
#     if index ==0:
#         print("커피는 폐기처분 되었습니다.")


# customer = "민규"
# index = 1
# while True:
#     print("{0}님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index+=1



# customer = "원우"
# person = "Unknown"

# while person != customer:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요 ? : ")
#     print("맛있게드세요 :)")


    
#<------------------------------------------------------------->
#coutinue  / break

# absent = [2,5]  #결석
# for std in range(1,11):
#     if std in absent :
#         continue
#     print("{0}야 책을 읽어봐".format(std))

# no_book = [7] #책을 안가져온 학생

# for std in range(1,11):
#     if std in absent :
#         continue
#     elif std in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(std))
#         break
#     print("{0}야 책을 읽어봐".format(std))


#<------------------------------------------------------------->
# 출석번호 101 102 103 ...
# std = [1,2,3,4,5]
# print(std)

# std = [i+100 for i in std]
# print(std)


# 학생 이름을 길이로 반환
# std = ["mina","young",'jun']
# print(std)

# std = [len(i) for i in std]
# print(std)

# 학생 이름 대문자로 변환 --> upper()
# std = ["mina","young",'jun']
# std = [i.upper() for i in std]
# print(std)


#<------------------------------------------------------------->
# quiz. 택시를 이용하는 택시 기사라고 가정
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램 작성
# 조건 1 : 승객별 운행 소요 시간은 5분~50분 사이 난수
# 조건 2 : 당신은 소요 시간 5~분15분 사이의 승객만 매칭

from random import *

count = 0  #총 탑승 승객 수
for person in range (1,51): # 1명 ~ 50명 승객 수
    time = randrange(5,51)  # 5분 ~ 50분 사이 
    if 5 <=time <=15:   # 매칭 성공
        print("[O] {0}번째 손님 ( 소요시간 : {1}분)".format(person, time))
        count +=1
    else :  # 매칭 실패
         print("[ ] {0}번째 손님 ( 소요시간 : {1}분)".format(person, time))
    
print("\n총 탑승객 : {0} 분".format(count))
