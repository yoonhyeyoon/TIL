# 정식이의 은행업무

def get_int(s, i):
    s[i] = 1 - s[i]  # i 번째 자리 바꿈
    sum = 0
    for t in range(len(s)):
        sum *= 2
        sum += s[t]

    s[i] = 1 - s[i]  # 원상복구
    return sum

def get_three_0(s, i):
    tmp = s3[i]
    s3[i] = 0
    sum = 0
    for t in range(len(s)):
        sum *= 3
        sum += s[t]
    s3[i] = tmp
    return sum

def get_three_1(s, i):
    tmp = s3[i]
    s3[i] = 1
    sum = 0
    for t in range(len(s)):
        sum *= 3
        sum += s[t]
    s3[i] = tmp
    return sum

def get_three_2(s, i):
    tmp = s3[i]
    s3[i] = 2
    sum = 0
    for t in range(len(s)):
        sum *= 3
        sum += s[t]
    s3[i] = tmp
    return sum

T = int(input())

for tc in range(1, T+1):
    s2 = list(map(int, input()))
    s3 = list(map(int, input()))

    ret1 = []
    ret2 = []
    for i in range(len(s2)):
        ret1.append(get_int(s2, i))  # s 의 i 번째 자리 바꾸기

    for j in range(len(s3)):
        if s3[j] == 0:
            ret2.append(get_three_1(s3, j))
            ret2.append(get_three_2(s3, j))

        if s3[j] == 1:
            ret2.append(get_three_0(s3, j))
            ret2.append(get_three_2(s3, j))

        if s3[j] == 2:
            ret2.append(get_three_0(s3, j))
            ret2.append(get_three_1(s3, j))


    for k in range(len(ret1)):
        if ret1[k] in ret2:
            ans = ret1[k]

    print("#{} {}".format(tc, ans))

# 방법 2 - 리스트를 뒤집어 ^ 연산