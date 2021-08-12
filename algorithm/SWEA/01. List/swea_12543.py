tc = int(input())

for test in range(1, tc+1):
    a = list(range(1, 12+1))
    set_cnt, set_sum = map(int, input().split())  # 부분집합 원소 개수 # 부분집합 원소의 합
    result = 0

    for bit in range(1 << 12):  # bit 만들기
        total = 0
        cnt = 0
        for i in range(12):
            if bit & (1 << i):
                total += a[i]
                cnt += 1
        if total == set_sum and cnt == set_cnt:
            result += 1
    print(result)