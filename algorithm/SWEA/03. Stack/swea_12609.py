# 스택 연습

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print("#{}".format(tc))
    lst = []
    for i in range(n):
        a = input().strip()
        if 'i' in a:
            lst.append(a[2:])
        elif a == 'c':
            print(len(lst))
        elif a == 'o':
            if len(lst) == 0:
                print('empty')
            else:
                o = lst.pop()
                print(o)