#negatives, zeros and positive
def numbersList(t):
    #create empty lists where insert the negative values, the zero values and the positive values
    n_list = []
    z_list = []
    p_list = []
    for i in t:
        if i < 0:
            n_list.append(i)
        elif i > 0:
            p_list.append(i)
        else:
            z_list.append(i)

    return n_list, z_list, p_list

def main():
    user_list = []
    user_input = input("Insert an integer number (blank to quit): ")
    while user_input != "":
        user_list.append(int(user_input))
        user_input = input("Insert an integer number (blank to quit): ")

    n_list, z_list, p_list = numbersList(user_list)
    for negative in n_list:
        print(negative)
    for zeros in z_list:
        print(zeros)
    for positive in p_list:
        print(positive)


if __name__ == "__main__":
    main()

