# 평균

n = int(input())
n_list =  list(map(int, input().split()))
max_list = max(n_list) 

for i in range(n):
    n_list[i] = n_list[i] / max_list * 100
    
print(sum(n_list) / n)