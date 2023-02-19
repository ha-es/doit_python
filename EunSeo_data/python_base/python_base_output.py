# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10 자리 공간을 확보

# 500을 출력하되
# ' ' 빈공간을
# > 오른쪽 정렬로
# 10 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 + 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(-500))

# 왼쪽 정렬후 빈칸 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마 찍어주기  --> 숫자 자리 수
print("{0:,}".format(100000000000000))

# 3자리마다 콤마 찍어주기, +- 부호 붙이기
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

# 3자리마다 콤마 찍어주기, 부호 붙이고, 자릿수도 확보
# 빈자리는 ^로 채우기
print("{0:^<+30,}".format(-100000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자릿수 까지 출력 --> 소수접 3째자리에서 반올림
print("{0:.2f}".format(5/3))