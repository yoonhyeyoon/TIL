# 삼성시의 버스 노선

# 방법 1
T = int(input())
for tc in range(1, T+1):
    n = int(input())

    lst1 = [0] * 5001 # 출발
    lst2 = [0] * 5001 # 도착

    for t in range(n):
        s, e = map(int, input().split())
        lst1[s] += 1
        lst2[e] += 1

    p = int(input())

    lst3 = [0] * 5001 # 정류장

    for b in range(len(lst3)-1):
        lst3[b+1] = lst3[b] - lst2[b] + lst1[b+1]

    print("#{}".format(tc), end=" ")
    for _ in range(p):
        c = int(input())
        print(lst3[c], end=" ")
    print()

# 방법2 누적시켜서 더해놓기
    bus_stop = [0] * 5001 # 정류장

    for t in range(n):
        s, e = map(int, input().split())
        for j in range(s, e+1):
            bus_stop[j] += 1 # 정류장에 버스노선 기록
