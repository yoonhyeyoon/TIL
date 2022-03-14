def solution(n, lost, reserve):
    answer = 0

    _lost = set(lost) - set(reserve) # 차집합
    _reserve = set(reserve) - set(lost)
    
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
            
    answer = n - len(_lost)
    
    return answer