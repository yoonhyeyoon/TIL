from itertools import permutations
def is_prime_number(n):
    if n == 0 or n == 1 : return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        nss = list(permutations(numbers, i))
        for ns in nss:
            n = int("".join(ns))
            if is_prime_number(n):
                answer.append(n)
                
    answer = len(list(set(answer)))
    
    return answer