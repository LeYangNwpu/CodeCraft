# Python3 program to find the maximum stolen value

# calculate the maximum stolen value
def maximize_loot(hval, n):
    if n == 0:
        return 0

    value1 = hval[0]
    if n == 1:
        return value1

    value2 = max(hval[0], hval[1])
    if n == 2:
        return value2

    # contains maximum stolen value at the end
    max_val = None

    # Fill remaining positions
    for i in range(2, n):
        max_val = max(hval[i] + value1, value2)
        value1 = value2
        value2 = max_val

    return max_val


# Driver to test above code
def main():
    # Value of houses
    hval = [6, 7, 1, 3, 8, 2, 4]

    # number of houses
    n = len(hval)
    print("Maximum loot value : {}".format(maximize_loot(hval, n)))


if __name__ == '__main__':
    main()
