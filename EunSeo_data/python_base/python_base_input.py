# sep -> 각 , 사이에 들어감
# end -> 한 줄롤 출력  / 문장의 끝 부분을 파라미터 값으로

import sys
# print ("python", "java", sep=",", end="?")
# print("무엇이 더 재미있을까? ")

# print ("python", "java", file=sys.stdout)   # 표준 출력
# print ("python", "java", file=sys.stderr)   # 표준 에러 / 필요 시 따로 에러처리 가능

# 시험 성적
# scores = {"수학" :0, "영어":50, "코딩":100}
# for sub, score in scores.items():
#     #print(sub, score)
#     # ljust -> n칸의 공간 확보 후 왼쪽 정렬
#     # rjust -> n칸의 공간 확보 후 오른쪽 정렬
#     print(sub.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기순번표
# 001, 002, 003 ...

# zfill() -> n크기만큼 공간확보 후 값이 없는 빈공간은 0을 채움
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))


answer = input("값을 입력하세요  : ") 
print(type(answer)) # input()은 항상 문자열로 저장!
print("입력하신 값은 " +answer + "입니다.")