# A+B -4

import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    try:
        print(a+b)
    except:
        break
