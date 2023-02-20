# 매 번 close()할 필요가 없음

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    
# close( )문 필요 없음


# with open ("study.txt","w",encoding="utf8") as study_file:
#         study_file.write("파이썬을 공부하고 있어요.")

with open ("study.txt","r",encoding="utf8") as study_file:
        print(study_file.read())
        
        
        
#<------------------------------------------------------------->
# quiz. 매 주 1회 작성해야 하는 보고서가 있다. 보고서의 형식대로 출력

# - x 주차 주간 보고 -
# 부서 : 
# 이름 : 
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일 만드는 프로그램 작성
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만들기


# for i in range(1,51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0}주차 주간 보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 :")
        

