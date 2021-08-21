# 비밀번호

T = 10

for tc in range(T):
    n, char = input().split()
    n = int(n)
    password = []

    for i in range(n):
        if password:
            if char[i] == password[-1]:
                password.pop()
            else:
                password.append(char[i])
        else:
            password.append(char[i])

    print("#{}".format(tc), ''.join(password))