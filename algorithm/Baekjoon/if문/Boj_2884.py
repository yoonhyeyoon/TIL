# 모닝콜 45분 더 앞당기기 

H, M = map(int, input().split())

if M < 45: 
    if H == 0:
        H = 23
    else:
        H = H -1 
    M += 15 
else:
    M -= 45

print(H, M)