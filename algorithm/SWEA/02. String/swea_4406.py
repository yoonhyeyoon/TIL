# 모음이 보이지 않는 사람

T = int(input())

for tc in range(1, T+1):
    string = input()
    result = ""
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(string):
        if i not in vowels:
            result += i

    print("#{} {}".format(tc, result))