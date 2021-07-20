# 각 자리수가 짝수인 숫자를 찾아 (,)로 구분하기

result = ""

for i in range(100,301):
    temp_100 = int(i / 100) # 첫째자리 수
    temp_10 = int(i / 10)  # 둘째자리 수
    temp_1 = int(i / 1)   # 셋째자리 수
    if temp_100 % 2 == 0 and temp_10 % 2 == 0 and temp_1 % 2 == 0:
        result += f"{i},"

print(result[:len(result)-1])

