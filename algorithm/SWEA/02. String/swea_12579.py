# 앞글자 따기

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    string = list(input().split())

    new_str = ""
    for i in range(n):
        new_str += string[i][0].upper()

    print(new_str)
