# 벌집

n = int(input())

x = 1
z = 1

while x < n:
    x += 6 * z
    z += 1
print(z)