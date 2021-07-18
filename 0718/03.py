# *******
#  *****
#   ***
#    *

k,i = 0,7
while i > 0:
    print("{0}{1}".format(" " * k, "*" * i))
    i -= 2
    k += 1

#     *
#    **
#   ***
#  ****
# *****

for i in range(1, 6):
    print("{0:>5}".format("*" * i))