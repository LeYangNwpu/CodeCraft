'''
Problem:
    Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
    By convention, 1 is included.
'''

# for DP solution, rather than loop through all natural number
# and check whether it is ugly number, we plan to construct the ugly number one by one
# precisely, we should maintain 3 pointers {i2, i3, i5} and 3 next values{next_mulp_2,
# next_mulp_3, next_mulp_5}. each time we select the minimum from these 3 nxt values and
# updata the corresponding pointer.
# next_mulp_i = ugly_data[pointer_i] * i
# pointer += 1
def ugly_number_DP(n):
    ugly_data = [0] * (n)
    ugly_data[0] = 1

    i2 = i3 = i5 = 0
    next_mulp_2 = 2
    next_mulp_3 = 3
    next_mulp_5 = 5

    # notice: 
    #   for each i, we should use 3 separated if, rather than if--elif--else
    #   because there may exists equal numbers {next_mulp_2, next_mulp_3, next_mulp_5}
    for i in range(1, n):
        ugly_data[i] = min(next_mulp_2, next_mulp_3, next_mulp_5)
        if ugly_data[i] == next_mulp_2:
            i2 += 1
            next_mulp_2 = ugly_data[i2] * 2
        if ugly_data[i] == next_mulp_3:
            i3 += 1
            next_mulp_3 = ugly_data[i3] * 3
        if ugly_data[i] == next_mulp_5:
            i5 += 1
            next_mulp_5 = ugly_data[i5] * 5
    return ugly_data

print(ugly_number_DP(150))


