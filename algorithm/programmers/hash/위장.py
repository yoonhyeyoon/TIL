def solution(clothes):
    answer = 0
    hash_map = {}
    
    for _, cloth in clothes:
        if cloth in hash_map:
            hash_map[cloth] += 1
        else:
            hash_map[cloth] = 1
    
    temp = 1
    for cnt in hash_map.values():
        temp *= (cnt+1)
    answer = temp - 1
        
    return answer