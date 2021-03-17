#shipping calculator

def shipping_charge(i):
    first_item = 10.95
    other_item = 2.95
    if i <= 1:
        total = i * first_item
        return total
    else:
        other_items_charge = (i-1) * other_item
        total = first_item + other_items_charge
        return total

def main():
    items = int(input("Insert the number of items: "))
    charge = shipping_charge(items)
    print("The total shipping charge for",items,"items is %.2f$" % charge)

main()
