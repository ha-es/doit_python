# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}"\
#         .format(name, age, main_lang))
    


# profile("원우", 20, "파이썬")
# profile("민규",22,"자바")


# 같은 학교, 학년, 반, 수업
# 이름만 다르고 다른 건 다 같음
# 이럴 땐 기본값 사용!

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이 : {1}\t 주 사용 언어 : {2}"\
#         .format(name, age, main_lang))
    
# profile("원우")
# profile("민규",22)


#<------------------------------------------------------------->
# 키워드 값

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# 키워드 = 값
# 순서가 뒤섞여 있어도 함수 순서대로 출력    
# profile(name ="원우",  main_lang="파이썬", age=20)


#<------------------------------------------------------------->
# 가변인자

# def profile(name, age, lan1, lan2, lan3, lan4, lan5):
#     print("이름 : {0} \t 나이 : {1}\t".format(name, age), end=" ")
#     print(lan1, lan2, lan3, lan4, lan5)

def profile(name, age, *language):
    print("이름 : {0} \t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()
    
profile("원우", 20, "파이썬", "자바","C", "C++", "C#","자바 스크립트")
profile("민규", 21 , "kotiln", "자바")
