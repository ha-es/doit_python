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

absent = [2,5]  #결석
# for std in range(1,11):
#     if std in absent :
#         continue
#     print("{0}야 책을 읽어봐".format(std))

for std in range(1,11):
    if std in absent :
        break
    print("{0}야 책을 읽어봐".format(std))
    