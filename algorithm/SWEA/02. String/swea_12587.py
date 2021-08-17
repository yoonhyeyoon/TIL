# 글자 수

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_cnt = 0

    for s in range(len(str1)):
        cnt = 0
        for t in range(len(str2)):
            if str1[s] == str2[t]:
                cnt += 1
        
        if max_cnt < cnt:
            max_cnt = cnt
        
    print("#{} {}".format(max_cnt))