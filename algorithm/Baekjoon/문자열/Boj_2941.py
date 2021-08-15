# 크로아티아 알파벳

alphabet = input()
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0

for l in lst:
    if l in alphabet:
        alphabet = alphabet.replace(l,'*')


print(len(alphabet))

