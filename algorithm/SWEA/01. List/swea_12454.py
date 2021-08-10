# 전기버스

tc = int(input())

for test in range(tc):
    k, n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    is_charge = [0] * 100
    for i in tmp:
        is_charge[i] += 1 # DAT 기법

    point = 0
    cnt = 0
    flag = 0
    while point < n:
        flag = 0
        # k 칸 검사 point+1 point+2 ... point+k
        charge = point
        for i in range(1, k+1):
            if point + i == n: # 다왔으면? 끝
                flag = 0
                break
            if is_charge[point + i] == 1:
                charge = point + i
                flag = 1 # 가장 멀리 있는 곳이 기록됨
        if flag == 0: # 없으면? 중간 탈락
            break
        else: # 충전소 도착
            point = charge # 위치 변경
            cnt += 1 # 충전소 선택

    if point == n:
        print("#{} {}".format(test+1, cnt))
    else:
        print("#{} 0".format(test+1))
