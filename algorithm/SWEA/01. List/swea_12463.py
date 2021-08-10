# 구간합

tc = int(input())
for ttt in range(1, tc +1):
 
 
    N, M = map(int, input().split()) # M : 구간의 크기
    val = list(map(int,input().split()))  
 
    sum = 0
    for i in range(M): # 첫번째 구간 합 구하기
        sum += val[i]
 
    max_sum = sum
    min_sum = sum

    # sliding window
    a = 0 # 제거
    for b in range(M, N): # [M] ......[N-1] b 는 구간의 끝(추가)
        sum -= val[a]
        sum += val[b]
        if max_sum < sum :
            max_sum = sum
        if min_sum > sum :
            min_sum = sum
        a += 1
 
        ans= max_sum - min_sum
    print('#{} {}'.format(ttt, ans))
