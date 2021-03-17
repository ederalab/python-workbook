#decimal to binary
result = ""
q = int(input("Insert the decimal number: "))

while q != 0 :
    r = q % 2
    r = str(r)
    result = r + result
    q = q // 2

print("The corresponding binary number is",result)