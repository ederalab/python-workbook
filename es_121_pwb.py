#random lottery numbers

from random import randint

min_num = 1
max_num = 49
ext_num = 6

lottery = []

for i in range(ext_num):
    n = randint(min_num, max_num + 1)
    while n in lottery:
        n = randint(min_num, max_num + 1)

    lottery.append(n)

lottery.sort()

print("The lottery numbers are: ")
for i in lottery:
    print(i, end=" ")