# 피보나치 수 5

n = int(input())

def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 2) + fibo(num -1)

print(fibo(n))