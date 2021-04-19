#reduce measures

def reduce(n, u):
    u = u.lower()
    tsp_per_tbsp = 3
    tsp_per_cups = 16 * tsp_per_tbsp
    if u == "teaspoon" or u == "teaspoons" or u == "tsp":
        tsp = n
    elif u == "tablespoon" or u == "tablespoons" or u == "tbsp":
        tsp = n * tsp_per_tbsp
    elif u == "cups" or u == "cup":
        tsp = n * tsp_per_cups
    else:
        print("insert a correct unit of measure")
        quit()

    cups = tsp // tsp_per_cups
    tsp = tsp - cups * tsp_per_cups
    tbsp = tsp // tsp_per_tbsp
    tsp = tsp - tbsp * tsp_per_tbsp

    result = ""

    if cups > 0:
        result = result + str(cups) + " cup"
        if cups > 1:
            result = result + "s"
    if tbsp > 0:
        if result != "":
            result = result + ", "
        result = result + str(tbsp) + " tablespoon"
        if tbsp > 1:
            result = result + "s"
    if tsp > 0:
        if result != "":
            result = result + ", "
        result = result + str(tsp) + " teaspoon"
        if tsp > 1:
            result = result + "s"
    if result == "":
        result = "0 teaspoons"

    return result


def main():
    unit_number = int(input("Insert the units: "))
    unit_measure = input("Insert the unit measure: ")
    result = reduce(unit_number,unit_measure)
    print("The conversion is",result)


if __name__ == "__main__":
    main()
