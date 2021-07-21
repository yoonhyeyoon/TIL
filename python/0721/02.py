# 피보나치 수열

# 재귀함수 이용 

# def fib(num):
#     if num < 2:
#         return num
#     else:
#         return fib(num-2) + fib(num-1)

# print(fib(10))

def fib(num):
    lst = [1] * num
    for i in range(num):
        if i < 2:
            pass
        else:
            lst[i] = lst[i-2] + lst[i-1]
    print(lst)

fib(int(input()))