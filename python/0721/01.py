# 소수 판별하기

def decimal(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt <= 2:
        print("소수입니다.")

decimal(int(input("값을 입력하세요." )))
