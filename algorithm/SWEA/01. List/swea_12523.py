# 델타검색

tc = 10

for test in range(1, tc+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    total = 0

    for i in range(n):
        for j in range(len(nums)):
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0 <= ni < n and 0 <= nj < len(nums):
                    if nums[i][j] >= nums[ni][nj]:
                        total += nums[i][j] - nums[ni][nj]
                    else:
                        total += nums[ni][nj] - nums[i][j]

    print(f'#{test} {total}')

