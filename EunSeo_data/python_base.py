#리스트 []
subway = [10,20,30]
subway = ["원우","민규","승관"]
print(subway)

#승관이 몇 번째 칸에 타고 있는가?
print(subway.index("승관"))

#호시가 다음 정류장에서 다음 칸에 탑승했을 경우
# append() 항상 맨 뒤에 추가!
subway.append("호시")
print(subway)

# 정한 / 민규와 승관사이에 추가하기
subway.insert(2,"정한")
print(subway)

# 지하철에 있는 사람을 한 명씩 빼기 -> pop()
print(subway.pop())
print(subway)

# 동일 인물이 몇 명있는지
subway.append("원우")
print(subway.count("원우"))


# 정렬도 가능
# sort()
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)


# # 순서 뒤집기 -> 반대로 출력
# # reverse()
num_list.reverse()
print(num_list)

# # 모두 지우기
num_list.clear()
print(num_list)



# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["원우",20, True]
print(mix_list)

# 리스트 확장 (합치기)
# extend()
num_list.extend(mix_list)
print(num_list)