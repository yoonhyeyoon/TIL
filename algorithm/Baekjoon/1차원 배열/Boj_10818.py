# 최소, 최대

n = int(input())
lst = list(input().split())

n_lst = []
for i in range(n):
    n_lst.append(int(lst[i]))
print(min(n_lst), max(n_lst))