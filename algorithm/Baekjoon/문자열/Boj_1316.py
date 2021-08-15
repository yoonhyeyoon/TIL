# 그룹 단어 체커

T = int(input())
ans = 0

for tc in range(T):
    word = input()
    lst = [word[0]]
    check = word[0]
    for w in word:
        if w != check:
            check = w
            lst.append(w)
            if lst.count(w) > 1:
                break
    else:
        ans += 1

print(ans)
