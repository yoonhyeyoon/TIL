# 달팽이는 올라가고 싶다

import math
a, b, v = map(int, input().split())

cnt = (v - b) / (a - b) 
# 분모는 올라갔다가 미끄러지는 걸로 계산
# 하지만 마지막 날에는 미끄러지기 전에 도달하기때문에 v-b만큼 올라가는 것이다.

print(math.ceil(cnt))