#below and above average

def average(t):
    t_below = []
    t_above = []
    t_average = []
    for n in t:
        if n < sum(t) / len(t):
            t_below.append(n)
        elif n > sum(t) / len(t):
            t_above.append(n)
        else:
            t_average.append(n)

    return t_below, t_average, t_above


def main():
    t = []

    n = input("Insert a series of numbers (blank line to quit): ")
    while n != "":
        t.append(float(n))
        n = input("Insert a series of numbers (blank line to quit): ")

    t_below,t_average,t_above = average(t)
    n_average = sum(t) / len(t)
    print("The average of the number you submitted is", n_average)
    print("Numbers below the average: ")
    for n in t_below:
        print("->",n)

    if t_average != []:
        print("Numbers equals the average: ")
        for n in t_average:
            print("->",n)

    print("Numbers above the average: ")
    for n in t_above:
        print("->",n)


if __name__ == "__main__":
    main()

