# 부분집합 합

tc = 10

for test in range(1, tc+1):
    n = int(input())
    set_num = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << n): # bit 만들기
        total = 0
        for j in range(n + 1):  # set_num 돌리기
            if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
                total += set_num[j]
        if total == 0:
            cnt += 1
    print("#{} {}".format(test, cnt))