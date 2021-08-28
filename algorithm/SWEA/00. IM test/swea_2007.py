# 패턴 마디의 길이

T = int(input())

for tc in range(1, T+1):
    patten = input().strip()
    ans = 0
    for i in range(10):
        if patten[0] == patten[i]:
            if patten[10] == patten[i+10]:
                ans = i
                
    print("#{} {}".format(tc, ans))