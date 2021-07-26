# (세 자리 수) × (세 자리 수)

num_1 = int(input())
num_2 = int(input()) # input() str으로 받아서 
num_3 = num_1 * (num_2%10) # num_1 * int(num2[2]) slicing 으로 계산
num_4 = num_1 * ((num_2//10)%10)
num_5 = num_1 * (num_2//100)
num_6 = num_1 * num_2

print(num_3)
print(num_4)
print(num_5)
print(num_6)