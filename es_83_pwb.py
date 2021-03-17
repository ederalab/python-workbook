#maximum integer
import random
i = 1
updates = 0
while i <= 100:
    n = random.randint(1, 100)
    if i == 1:
        max_val = n
        print(n)
    else:
        if n > max_val:
            max_val = n
            updates += 1
            print(n,"<== Update")
        else:
            print(n)
    i += 1

print("The maximum value found was", max_val)
print("The maximum value was updated", updates,"times")
