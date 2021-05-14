# greatest common divisor

def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return greatest_common_divisor(b, c)

print(greatest_common_divisor(123456, 67890))