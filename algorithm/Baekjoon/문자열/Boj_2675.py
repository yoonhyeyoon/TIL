# 문자열 반복

tc = int(input())

for test in range(tc):
    r, s = input().split()
    for i in range(len(s)):
        print(s[i]*int(r),end="")
    print()
