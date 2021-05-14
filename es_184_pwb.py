# flatten a list

def flatten(data):
    if data == []:
        return data
    if type(data[0]) == list:
        l1 = flatten(data[0])
        l2 = flatten(data[1:])
        return l1 + l2
    else:
        l1 = []
        l1.append(data[0])
        l2 = flatten(data[1:])
        return l1 + l2


def main():
    mylist = [["uno", "due", "tre"], 1, [2, 3], [4, [5, 6, 7], 8], [9, 10]]
    #mylist = [1, [2, 3], [4, [5, 6, 7], 8], [9, 10]]
    flatten_list = flatten(mylist)
    print("This is the flattened list: ", flatten_list)


if __name__ == '__main__':
    main()