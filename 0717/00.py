# 가위바위보 게임

Man1 = input()
Man2 = input()

if Man1 == '가위':
    if Man2 == '가위':
        print("Result : Draw")
    elif Man2 == '바위':
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
elif Man1 == '바위':
    if Man2 == '바위':
        print("Result : Draw")
    elif Man2 == '보':
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
else:
    if Man2 == '보':
        print("Result : Draw")
    elif Man2 == '가위':
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")