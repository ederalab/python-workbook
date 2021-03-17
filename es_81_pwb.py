#binary to decimal
binary = input("Insert the binary number: ")
i = len(binary) -1
j= 0
decimal = 0
while i >= 0:
    n = binary[j]
    n = int(n)
    compute = n * (2**i)
    decimal = decimal + compute
    i = i - 1
    j = j + 1

print("The decimal number is", decimal)