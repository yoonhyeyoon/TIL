# 다이얼

dir = input()

lst = ['ABC','DEF','GHI','JKL','NMO','PQRS','TUV','WXYZ']

time = 0
for l in range(len(lst)):
    for s in range(len(lst[l])):
        for d in dir:
            if d == lst[l][s]:
                time += l + 3

print(time)
