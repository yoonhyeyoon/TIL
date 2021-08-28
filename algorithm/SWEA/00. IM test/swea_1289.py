# 원재의 메모리 복구하기

# 방법1
T = int(input())

for tc in range(1, T+1):
    memory = list(map(int, input()))
    n = len(memory)
    base = [0] * n

    for i in range(n):
        if memory[i] == 1:
            start = i
            break

    ans = 0
    for i in range(start, n):
        if base[i] == 0:
            if memory[i] == 1:
                for j in range(i, n):
                    base[j] = 1
                ans += 1
        if base[i] == 1:
            if memory[i] == 0:
                for j in range(i, n):
                    base[j] = 0
                ans += 1

    print("#{} {}".format(tc, ans))

# 더 간단한 방법2
    for i in range(n):
        if base[i] != memory[i]:
            for j in range(i, n):
                base[j] = memory[i]
            ans += 1