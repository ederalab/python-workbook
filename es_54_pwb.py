#assessing employees
performance = input("How was the performance of the employer?")
performance = str.lower(performance)

multiply = 2400
if performance == "unacceptable":
    rating = multiply * 0.0
    print("the raise will be:", rating)
elif performance == "acceptable":
    rating = multiply * 0.4
    print("the raise will be:", rating,"$")
elif performance == "meritorious":
    rating = multiply * 0.6
    print("the raise will be:", rating,"$")
else:
    print ("You insert an invalid rating")
