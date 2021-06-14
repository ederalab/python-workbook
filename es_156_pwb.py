# Sum a Collection of Numbers

def main():
    total = 0
    n = input("Please enter a number (blank line to quit): ")

    while n != "":
        try:
            total += float(n)
            print('you entered a valid number:',n)
            print('the subtotal is:', total)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

        n = input("Please enter a number (blank line to quit): ")

    print('The total sum of the number you entered is:', total)


if __name__ == '__main__':
    main()