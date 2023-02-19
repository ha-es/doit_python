# 지역 변수 ( = 함수 내에서만 사용 )
# 전역 변수 ( = 모든 공간에서 사용 )

# gun =10

# def checkpoint(solodiers):  #경계근무
#     #gun =20
#     global gun      #전역 공간에 있는 gun 사용
#     gun -= solodiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
  
 
 
# def  checkpoint_ret(gun, solodiers):
#     gun -= solodiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# # 함수 내의 변수 = 지역변수    
# print("전체 총의 수 : {0}".format(gun))
# #checkpoint(2)
# gun = checkpoint_ret(gun, 2)


# # 함수 밖의 변수 = 전역변수
# print("남은 총 : {0}".format(gun))



#<------------------------------------------------------------->
# quiz. 표준 체중을 구하는 프로그램 작성
# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시 -> round()


def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height*height*22

    else:
           return height*height*21


height = 175 #cm 단위
gender = "남자"

weight = round(std_weight(height/100, gender),2) # 키 cm -> m 단위 변환
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
