# weather = input("오늘 날씨 어때요? :")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# else :
#     print("필요 없어요")
    

# input( )은 문자열로 받기 때문에 int를 써줘야함
temp = int(input("오늘 기온은 어때요? : "))

if 30 <= temp:
    print("너무 더운 날씨에요.")
elif 10<= temp and temp <30 :
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else : 
    print("너무 추운 날씨에요.")