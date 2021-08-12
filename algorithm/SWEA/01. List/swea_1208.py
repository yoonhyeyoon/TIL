tc = 10

for test in range(1, tc+1):
    dump_cnt = int(input())
    box = list(map(int, input().split()))
    n = len(box)
    
    # 선택정렬
    for i in range(n):
        for j in range(i, n):
            if box[i] > box[j]:
                box[i], box[j] = box[j], box[i]

    for dump in range(dump_cnt):
        box[0] += 1
        box[n-1] -= 1

        # 자기자리 찾기
        left = 0
        while left + 1 < n and box[left] > box[left+1]:
            box[left], box[left+1] = box[left+1], box[left]
            left += 1
        right = n-1
        while right - 1 >= 0 and box[right] < box[right-1]:
            box[right], box[right-1] = box[right-1], box[right]
            right -= 1

    print("#{} {}".format(test, box[n-1]-box[0]))