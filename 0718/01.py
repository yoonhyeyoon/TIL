# 짝수 출력하기

for i in range(1, 101):
    if i % 2 ==0:
        print(f"{i} ",end="")

# 홀수 출력하기

num = ""
for i in range(1, 101):
    if i % 2 ==1:
        num += f"{i}, " 
print(num[:-2])

# 3의 배수의 총합 구하기

total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
print("1부터 100사이의 숫자 중 3의 배수의 총합: %d" % (total))