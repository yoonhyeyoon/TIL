# 최소 이동 거리

def dijkstra():
    dist = [987654321] * (V+1)
    visited = [0] * (V+1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        # 최소값 찾기
        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1
        # 갱신할 수 있으면 갱신
        for i in range(V+1):
            if not visited[i] and dist[i] > dist[min_idx] + adj[min_idx][i]: ## dist[min_idx] 도 같이 더해줄 것이냐가 Prim 과의 유일한 차이
                dist[i] = dist[min_idx] + adj[min_idx][i]

    return dist[V]

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    print("#{} {}".format(tc, dijkstra()))