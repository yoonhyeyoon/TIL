def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(0, len(phone_book)-1):
        if len(phone_book[i]) <= len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
                
    return answer


# 방법 2 (hash)
def solution(phone_book):
    answer = True
    phone_book.sort()
    hash_map = {}
    
    for phone_num in phone_book:
        hash_map[phone_num] = 1
        
    for phone_num in phone_book:
        temp = ''
        for num in phone_num:
            temp += num
            if temp in hash_map and temp != phone_num:
                answer = False
                break
            
    return answer