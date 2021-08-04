# 최댓값

max = 0
idx = 0
for i in range(9):
    n = int(input())
    if max < n:
        max = n
        idx = i
print(max)
print(idx+1)
    