#is a license plate valid?
# 3 uppercase + 3 digits
# 4 digits + 3 uppercase

lp = input("Insert the license plate: ")
lp_len = len(lp)
    
if lp_len == 6 and \
    lp[0] >= "A" and lp[0] <= "Z" and \
    lp[1] >= "A" and lp[1] <= "Z" and \
    lp[2] >= "A" and lp[2] <= "Z" and \
    lp[3] >= "0" and lp[3] <= "9" and \
    lp[4] >= "0" and lp[4] <= "9" and \
    lp[5] >= "0" and lp[5] <= "9": 
    message = "The license plate you submitted is valid for the older style"
elif lp_len == 7 and \
    lp[0] >= "0" and lp[0] <= "9" and \
    lp[1] >= "0" and lp[1] <= "9" and \
    lp[2] >= "0" and lp[2] <= "9" and \
    lp[3] >= "0" and lp[3] <= "9" and \
    lp[4] >= "A" and lp[4] <= "Z" and \
    lp[4] >= "A" and lp[4] <= "Z" and \
    lp[4] >= "A" and lp[4] <= "Z":
    message = "The license plate you submitted is valid for the newer style"
else:
    message="The license plate you submitted is not valid"
print(message)
