# set (집합)
# 중복 안됨, 순서가 없음

my_Set = {1,2,3,3,3}
print(my_Set)

teamA = {"원우","민규","승관"}
teamB = set(["원우","호시"])

print(type(teamA))
print(type(teamB))

# 교집합 ( java + pyhon 모두 할 수 있는 사람)
print(teamA & teamB)
print(teamA.intersection(teamB))


# 합집합 (java도 할 수 있거나 python도 할 수 있는 사람)
print( teamA | teamB)
print(teamA.union(teamB))

# 차집합 ( java는 할 수 있지만 python은 하지 못하는 사람)
print(teamA - teamB)
print(teamA.difference(teamB))

# python할 수 있는 사람 추가
teamB.add("정한")
print(teamB)

# java를 할 수 있는 사람이 빠졌을 경우
teamA.remove("승관")
print(teamA)