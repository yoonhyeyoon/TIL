def solution(n, computers):
    answer = 0
    def dfs(i):
        # 방문처리
        computers[i][i] = 2
        for j in range(n):
            if computers[i][j] == 1 and computers[j][j] != 2:
                dfs(j)
    
    for i in range(n):
        if computers[i][i] != 2:
            dfs(i)
            answer += 1
    
    return answer