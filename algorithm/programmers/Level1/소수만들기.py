from itertools import combinations

def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    coms = list(combinations(nums, 3))
    for com in coms:
        if is_prime_number(sum(com)): answer += 1

    return answer

# 순열 from itertools import permutations
# 조합 from itertools import combinations
# 중복조합 from itertools import combinations_with_replacement