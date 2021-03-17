#caesar cipher
message = input("Insert the message you want to encrypt: ")
shift = int(input("Insert the shift to encrypt: "))

encrypt = ""

for letter in message:
    if letter >= "a" and letter <="z":
        pos = ord(letter) - ord("a")
        pos = (pos + shift) % 26
        l = chr(pos + ord("a"))
        encrypt = encrypt + l
    elif letter >= "A" and letter <="Z":
        pos = ord(letter) - ord("A")
        pos = (pos + shift) % 26
        l = chr(pos + ord("A"))
        encrypt = encrypt + l
    else:
        encrypt = encrypt + letter

print("The encrypt message is:", encrypt)
