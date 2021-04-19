# the sieve of eratosthenes
"""
technique to find all the prime numbers between 2 and some limit
"""

def sieve_eratosthenes(limit):
    num_list = []

    for n in range(0, limit + 1):
        num_list.append(n)

    num_list[1] = 0
    p = 2
    while p < limit:
        for i in range(p*2, limit + 1, p):
            num_list[i] = 0
        p = p + 1
        while p < limit and num_list[p] == 0:
            p = p + 1

    return num_list



def main():
    limit = int(input("Insert the limit to which identify all the prime numbers: "))
    result = sieve_eratosthenes(limit)
    for i in result:
        if result[i] != 0:
            print(result[i])


main()
