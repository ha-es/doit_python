cabinet = { 3 : "원우", 100: "민규"}
print(cabinet[3])
print(cabinet.get(3))

# cabinet[] -> error 발생 후 프로그램 종료
#print(cabinet[5])

# cabinet.get() -> None 출력, 프로그램 종료 되지 않음
# print(cabinet.get(5))
# 없으면 "사용 가능"이라고 출력  -> 쓸 수 있음
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# T / F 로 출력됨
# print(3 in cabinet)
# print(5 in cabinet)



cabinet2 = { "A-3" : "원우", "B-100": "민규"}
print(cabinet2["A-3"])
print(cabinet2)

# 새로 추가하기
# 값이 있다면 UPDATE (수정) --> 키가 중복되면 마지막 값으로 덮어씌워집니다.
cabinet2["C-20"] = "승관"
print(cabinet2)
cabinet2["B-100"] = "호시"
print(cabinet2)

# 값 삭제
del cabinet2["B-100"]
print(cabinet2)

# key값만 출력
print(cabinet2.keys())

# value만 출력
print(cabinet2.values())

# 쌍(Key-Value) 으로 출력
print(cabinet2.items())


# 삭제
cabinet2.clear()
print(cabinet2)
