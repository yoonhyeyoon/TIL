# 셀프 넘버

def self_number():
    generated_num = set()
    natural_num = set()
    for num in range(1, 10000+1):
        number = num
        for i in str(num):
            number += int(i)
        generated_num.add(number)
    
    for num in range(1, 10000+1):
        natural_num.add(num)
    self_numbers = sorted(natural_num - generated_num)
    
    for self_number in self_numbers:
        print(self_number)
        
self_number()