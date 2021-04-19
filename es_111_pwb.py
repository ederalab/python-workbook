#reverse order

mylist =[]
n = int(input("Insert an integer (0 to quit): "))
while n != 0:
    mylist.append(n)
    n = int(input("Insert an integer (0 to quit): "))

mylist.reverse()
for e in mylist:
    print(e)