# set (집합)
# 중복 안됨, 순서가 없음

my_Set = {1,2,3,3,3}
print(my_Set)

java = {"원우","민규","승관"}
python = set(["원우","호시"])

# 교집합 ( java + pyhon 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))


# 합집합 (java도 할 수 있거나 python도 할 수 있는 사람)
print( java | python)
print(java.union(python))

# 차집합 ( java는 할 수 있지만 python은 하지 못하는 사람)
print(java - python)
print(java.difference(python))

# python할 수 있는 사람 추가
python.add("정한")
print(python)

# java를 할 수 있는 사람이 빠졌을 경우
java.remove("승관")
print(java)