# 문자열의 거울상

T = int(input())

for tc in range(1, T+1):
    string = input()
    result = []

    for i in range(len(string)-1, -1, -1):
        if string[i] == 'b':
            result.append('d')
        elif string[i] == 'd':
            result.append('b')
        elif string[i] == 'p':
            result.append('q')
        else:
            result.append('p')

    
    print("#{} ".format(tc),end="")
    for s in range(len(result)):
    	print(result[s], end="")
    print()
   