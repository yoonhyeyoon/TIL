# 괄호검사

T = int(input())

for tc in range(1, T+1):
    n = input()
    s = len(n)
    i = 0
    lst = []
    check = 0
    while i < s:
        if n[i] == '(' or n[i] == '{':
            lst.append(n[i])
        elif n[i] == ')':
            if not lst:
                check = 1
            else:
                if lst[-1] != '(':
                    check = 1
                lst.pop()
        if n[i] == '}':
            if not lst:
                check = 1
            else:
                if lst[-1] != '{':
                    check = 1
                lst.pop()
        if check == 1:
            break
        i += 1

    if lst:
        check = 1

    if check == 0:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))