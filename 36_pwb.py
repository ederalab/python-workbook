#dog years
dog_years = int(input("insert human years and get the conversion: "))
if dog_years < 0:
    print("Attention, you insert a negative number")
elif dog_years >= 0 and dog_years <= 2:
    human_years = dog_years * 10.5
    print("The dog years is equivalent to human",human_years,"years old")
else:
    human_years = dog_years * 4
    print("The dog years is equivalent to human",human_years,"years old")