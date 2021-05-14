# possible change

from itertools import combinations_with_replacement

def change(d, c, i=0):
    coins = [0.25, 0.10, 0.05, 0.01]
    comb = list(combinations_with_replacement(coins, c))

    if d != round(sum(comb[i]), 4):
        i += 1
        if i >= len(list(comb)):
            return False, ""
        else:
            return change(d, c, i)
    else:
        return True, comb[i]


def main():
    amount = float(input("Insert the amount of dollars: "))
    coins = int(input("Insert the number of coins to change: "))
    result, combination = change(amount,coins)

    if result == True :
        print(f"You can change {amount}$ with {coins} coins: ")
        print(combination)
    else:
        print(f"It is not possible to change {amount}$ with {coins} coins")



if __name__ == "__main__":
    main()