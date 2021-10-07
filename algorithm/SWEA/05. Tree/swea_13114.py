# 퀵 정렬

def partition(s,e,lst) :
    pi = s
    small = s + 1
    big = e
    while small <= big :
        while small <= big and lst[pi] >= lst[small] : # 작은값 영역 넓히기  small ->
            small += 1
        while small <= big and lst[pi] <= lst[big] : # 큰값 영역 넓히기 <- big
            big -= 1
        if small < big :
            lst[small] , lst[big] = lst[big], lst[small] # swap
    lst[pi],lst[big] = lst[big],lst[pi]
    return big

def quick_sort(s,e,lst) :
    if s > e : return
    pivot = partition(s,e,lst) # 파티션하고 / pivot의 인덱스 return 받기
    quick_sort(s,pivot-1,lst)
    quick_sort(pivot+1,e,lst)
    return



T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    quick_sort(0,len(lst)-1,lst)
    print("#{} {}".format(tc, lst[n//2]))

