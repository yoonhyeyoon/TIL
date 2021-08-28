# 영준이의 카드 카운팅

T = int(input())

for tc in range(1, T+1):
    card = input()
    card_lst = {'S':0, 'D':1, 'H':2, 'C':3}
    ans = [13] * 4
    check = []
    ret = 1
    for i in range(0, len(card), 3):
        ans[card_lst[card[i]]] -= 1
        check.append((card[i:i+3]))

    if len(set(check)) != 4:
        ans = 'ERROR'
        ret = 0
        
    if ret:
        print(*ans)
    else:
        print(ans)