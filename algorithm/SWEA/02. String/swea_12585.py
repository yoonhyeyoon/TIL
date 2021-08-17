# 문자열 비교

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0

    for start in range(len(str2)-len(str1)+1):
        cnt = 0
        for p in range(len(str1)):
            if str2[start+p] != str1[p]:
                break
            cnt += 1
        if cnt == len(str1):
            ans = 1

    print("#{} {}".format(tc, ans))