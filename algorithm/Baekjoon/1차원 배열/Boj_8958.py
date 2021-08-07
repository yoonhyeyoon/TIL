# OX 퀴즈

n = int(input())

for _ in range(n):
    ox = input()
    score = 0
    c = 0
    for j in ox:
        if j == 'O':
            c += 1
            score += c
        else:
            c = 0
    print(score)

    

    
