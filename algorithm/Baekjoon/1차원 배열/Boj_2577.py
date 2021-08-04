# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

abc = a*b*c
abc = str(abc)

for i in range(10):
    print(abc.count(str(i)))