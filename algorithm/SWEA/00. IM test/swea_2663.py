# 백준
# 색종이

n = int(input())
MAP = [[0] * 101 for _ in range(101)]
 
for i in range(n):
    x, y = map(int, input().split())
    for y1 in range(10):
        for x1 in range(10):
            MAP[y+10-y1][x+x1] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if MAP[i][j] == 1:
            cnt += 1
 
print(cnt)