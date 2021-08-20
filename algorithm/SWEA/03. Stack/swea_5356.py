# 의석이의 세로로 말해요

T = int(input())
for tc in range(1, T+1):
    word = [0] * 5

    for i in range(5):
        word[i] = list(input())

    print("#{}".format(tc), end=" ")

    for j in range(15):
        for i in range(5):
            # 허락받고 쓰기
            # if len(word[i]) > j:
            #     print(word[i][j], end="")

            # 용서 구하기
            try:
                print(word[i][j], end="")
            except:
                pass
    print()
    