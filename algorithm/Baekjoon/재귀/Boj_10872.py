# 팩토리얼

n = int(input())

def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)

print(fact(n))