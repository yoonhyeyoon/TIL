# 후위 표기법

def check(a, b):
    rank = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
    if rank[a] < rank[b]:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    sic = input().rstrip()
    stack = []
    print("#{}".format(tc), end=' ')
    for i in range(len(sic)):
        if sic[i].isdigit():
            print(sic[i], end='')
        elif sic[i] == '(':
            stack.append(sic[i])
        elif sic[i] == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        else:
            while stack and not check(stack[-1], sic[i]):
                print(stack.pop(), end='')
            stack.append(sic[i])


    while stack:
        print(stack.pop(), end='')

    print()