# 알파벳 찾기

s = input()
lst = []

for j in range(97, 122+1):
    for i in range(len(s)):
        if chr(j) == s[i]:
            lst.append(i)
            print(lst)
            break
    else:
        lst.append(-1)

print(*lst)

