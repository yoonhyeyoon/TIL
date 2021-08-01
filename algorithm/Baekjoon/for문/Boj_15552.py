# 빠른 A+B
import sys 

t = int(input())

for i in range(t):
    # 반복문으로 input받을 때 사용하면 실행속도를 줄일 수 있다. 
    a, b = map(int, sys.stdin.readline().split())

    print(a + b)

    