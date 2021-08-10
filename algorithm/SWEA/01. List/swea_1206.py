# View

T = 10

for n in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    result = 0
    for i in range(2, N - 2):
        # height[i]
        # height[i-2] vs height[i -1] vs height[i + 1] vs height[i + 2]
        max_height = int(-21e8) # -21억
        if max_height < height[i - 2] :
            max_height = height[i - 2]
        if max_height < height[i - 1] :
            max_height = height[i - 1]
        if max_height < height[i + 1] :
            max_height = height[i + 1]
        if max_height < height[i + 2]:
            max_height = height[i + 2]

        tmp = height[i] - max_height

        if tmp > 0:
            result += tmp
        

    print(f'#{n} {result}')