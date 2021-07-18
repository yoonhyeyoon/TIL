# 10진수 -> 2진수 변환하기

n = int(input())
result = ""

while n > 0:
    result = str(n % 2) + result
    n //= 2
print(result)
