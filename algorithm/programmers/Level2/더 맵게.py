# Heap

import heapq # min-heap 형태 = 오름차순

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result # 오름차순된 정렬 결과


# 문풀

import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for value in scoville:
        heapq.heappush(h, value)
    
    while h[0] < K:
        if len(h) == 1:
            return -1
        heapq.heappush(h, heapq.heappop(h) + (heapq.heappop(h) * 2))
        answer += 1
        
    return answer