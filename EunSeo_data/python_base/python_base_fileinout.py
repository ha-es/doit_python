# open() - close()

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0점", file=score_file)
# print("영어 : 50점", file=score_file)
# score_file.close()

# 이미 존재하는 파일에다 이어서 쓰기 ( = append )
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80점\n")
# score_file.write("코딩 : 100점")
# score_file.close()

#<------------------------------------------------------------->

# 파일 내용 읽어오기
# 1. 한 번에 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()
#<------------------------------------------------------------->

# 2. 한 줄씩 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline())    # 줄별로 읽기, 한 줄일고 커서는 다음 줄로 이동
# #print(score_file.readline(), end ="")   # 줄바꿈 안함
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()
#<------------------------------------------------------------->

# 3. n줄인 파일 한 줄씩 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()
#<------------------------------------------------------------->

# 4. list에 값을 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  #list 향태로 저장
for line in lines:
    print(line, end="")

score_file.close()