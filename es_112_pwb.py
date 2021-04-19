#remove outliers
def removeOutliers(t, e):
    #make a copy of the list
    #sort the list to remove the largest and smallest elements

    tcopy = sorted(t)

    for i in range(e):
        tcopy.pop()

    for i in range(e):
        tcopy.pop(0)

    return tcopy


def main():
    min_elements = 4
    values_to_remove = int(min_elements / 2)
    print("Insert min", min_elements, "elements to the list.")
    user_list = []
    user_input = input("Insert a non-integer to the list (blank to quit): ")
    while user_input != "":
        user_list.append(float(user_input))
        user_input = input("Insert a non-integer to the list (blank to quit): ")

    if len(user_list) < min_elements:
        print("You insert less than", min_elements, "values.")
    else:
        removed_list = removeOutliers(user_list, values_to_remove)
        print(removed_list)
        print("The original list elements:")
        print(user_list)


if __name__ == "__main__":
    main()

