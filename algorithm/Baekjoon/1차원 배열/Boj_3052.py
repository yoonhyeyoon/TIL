# 나머지
result = []

for _ in range(10):
    n = int(input())
    if str(n % 42) not in result:
        result.append(str(n % 42))

print(len(result))