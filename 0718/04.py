#  0~9가 몇 번 사용되었는지 표시하기

num = int(input())
lst = [0] * 10

while num > 0:
    lst[num % 10] += 1
    num //= 10

for i in range(0, 10):
    print("%d " % i, end="")
print("")

for i in range(0, 10):
    print("%d " % lst[i], end="")