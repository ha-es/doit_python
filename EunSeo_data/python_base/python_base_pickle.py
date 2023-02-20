# 프로그램상에서 사용하고 있는 데이터를 파일형태로 저장
import pickle

# profile_file = open("profile.pickle","wb")    #저장
# profile = {"이름":"원우","나이":20,"취미":["게임","코딩","노래"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle","rb")  #읽기
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
