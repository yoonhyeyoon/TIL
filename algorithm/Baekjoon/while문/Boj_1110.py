# 더하기 사이클

n = int(input())
chk = n
cnt = 0
while True:
    nn = n // 10 + n % 10
    nn = (n % 10)*10 + nn % 10
    cnt += 1
    if chk == nn:
        print(cnt)
        break
    n = nn