# 약수 구하기

a = int(input())

list = [] # 약수 리스트
cnt = 0 # 약수 개수

for n in range(1, a+1):
    if a % n == 0:
        print("%d(은)는 %d의 약수입니다." % (n, a))
        cnt = cnt + 1
        list.append(n)

# 소수 판별하기

if cnt <= 2:
    print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (a, list[0], list[1]))
