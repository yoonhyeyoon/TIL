# 화물 도크

class schedule :
    def __init__(self, a,b):
        self.start = a
        self.end = b

def cmp(s_var):
    #s_var.start, s_var.end
    return (s_var.end,s_var.start) # end 시간 기준으로 오름차순 정렬

T = int (input())

for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N) :
        a,b = map(int, input().split())
        lst.append(schedule(a,b))

    # end 시간 기준으로 정렬하기
    lst.sort(key = cmp)
    de = -1

    cnt = 0
    now = 0

    # end시간이 빠른순서대로 선택이 된다 (정렬을 해놨으니까) -> 그리디
    for i in range(len(lst)) :
        # now < schedule.start
        if now <= lst[i].start :
            cnt += 1
            now = lst[i].end # now 갱신

    print("#{} {}".format(tc, cnt))