# 분수찾기

user_n = int(input())

n = 1
m = 1

while user_n > m:
    n += 1  # 각 대각선의 길이 
    m += n  # 각 대각선의 max 값

if n % 2 == 0:
    wk = n - (m - user_n)   # 분자
    ah = 1 + (m - user_n)   # 분모
    print(f'{wk}/{ah}')
elif n % 2:
    wk = 1 + (m - user_n)   # 분자
    ah = n - (m - user_n)   # 분모
    print(f'{wk}/{ah}')