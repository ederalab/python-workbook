# total the values

def total_values():
    total = 0.0
    val = input("Please, enter a number: (blank to quit): \n")
    if val == "":
        return total
    else:
        total += float(val)
        return total + total_values()

print(total_values())