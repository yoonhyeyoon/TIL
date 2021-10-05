# 컨테이너 운반

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    load = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    truck.sort(reverse=True)
    used = [0] * N

    ans = 0
    for t in range(M):
        idx = -1
        maxi = -int(21e8)
        
        for i in range(N):
            if used[i] == 1: continue
            if maxi < load[i] and truck[t] >= load[i]:
                maxi = load[i]
                idx = i
                
        if idx != -1:
            ans += load[idx]
            used[idx] = 1
            
    print("#{} {}".format(tc, ans))