# 단어 공부
# 방법 1 딕셔너리 이용
string = input()
base = {}
ans = []

string = string.upper()
for s in string:
    if s not in base:
        base[s] = 0
    elif s in base:
        base[s] += 1

for k, v in base.items():
    if max(base.values()) == v:
        ans.append(k)

# ------------------
# 방법2 set 이용
string = input()
string.upper()
check = set(string)
ans = []

for c in check:
    ans.append(string.count(c))
#--------------------

if len(ans) > 1:
    print("?")
else:
    print(*ans)

