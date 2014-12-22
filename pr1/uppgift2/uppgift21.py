#-*- coding: utf-8 -*-
# Hitta största palindrom tal med produkt av två 3-siffriga tal


def fastpal(number):
    return str(number) == str(number)[::-1]


def main():
    n = [-1]
    for i in range(1, 999):
        for k in range(1, 999):
            j = i * k
            # if i > 950 and k > 900 and k < 950:
            # print "%d * %d = %d" % (i, k, j)
            if fastpal(j) and j > n[0]:
                # print "%d is a palindrome" % j
                n = [j, i, k]
    print "%d (%d * %d) is the highest possible palindrome" % (n[0], n[1], n[2])
    return n[0]

if __name__ == '__main__':
    main()
