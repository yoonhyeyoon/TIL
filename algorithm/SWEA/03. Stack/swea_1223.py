# 계산기 2

def check(a, b):
    rank = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
    if rank[a] < rank[b]:
        return True
    else:
        return False


T = 10
for tc in range(1, T+1):
    n = int(input())
    sic = input().rstrip()
    stack = []
    back = ""
    print("#{}".format(tc), end=' ')
    # 중위표현식 -> 후위표현식
    for i in range(n):
        if sic[i].isdigit():
            back += sic[i]
        elif sic[i] == '(':
            stack.append(sic[i])
        elif sic[i] == ')':
            while stack[-1] != '(':
                back += stack.pop()
            stack.pop()
        else:
            while stack and not check(stack[-1], sic[i]):
                back += stack.pop()
            stack.append(sic[i])


    while stack:
        back += stack.pop()


    # 후위표현식 계산
    for i in range(n):
        if back[i].isdigit():
            stack.append(back[i])
        elif back[i] == '+':
            a = stack.pop()
            b = stack.pop()
            c = int(b) + int(a)
            stack.append(c)
        elif back[i] == '*':
            a = stack.pop()
            b = stack.pop()
            c = int(b) * int(a)
            stack.append(c)
    while stack:
        print(stack.pop())