# play bingo
from es_146_pwb import bingo_card
from es_147_pwb import check_winning_card
from random import randrange
import random
import copy


def bingo_calls():
    bingo_list = []
    sublist = []
    step = 15
    min = 1
    max = 1 + step

    while len(bingo_list) != 5:
        while len(sublist) != 5:
            n = randrange(min, max)
            if n not in sublist:
                sublist.append(n)
        bingo_list.append(sublist)
        sublist = []
        min = max + 1
        max = max + step

    return bingo_list


def check_cards(card, calls):
    keys = ["B", "I", "N", "G", "O"]
    check_card = copy.deepcopy(card)
    i = 0

    for key in keys:
        j = 0
        while j < len(check_card[key]):
            if check_card[key][j] in calls[i]:
                check_card[key][j] = 0
            j += 1
        i+= 1
    #print(check_card)
    check, mode = check_winning_card(check_card)
    return check, mode, check_card

def main():
    counts = 1000
    winning_cards = 0
    tot_calls = []
    card = bingo_card()
    for i in range(counts + 1):
        call = bingo_calls()
        result, mode, check_card = check_cards(card, call)
        if result == True:
            winning_cards += 1
            tot_calls.append(i)

    min_calls = min(tot_calls)
    max_calls = max(tot_calls)
    avg_calls = (max_calls - min_calls) / counts
    print(f"Out of {counts} calls, the minimum, maximum and average number before you have a winning card is: \n"
          "Minimum: {}".format(min_calls),
          "\nMaximum: {}".format(max_calls),
          "\nAverage: {:.2f}".format(avg_calls))


main()