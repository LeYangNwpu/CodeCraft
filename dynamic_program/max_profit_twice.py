'''
Probelm:
    Maximum profit by buying and selling a share at most twice.
Ways:
    Way 1:
        a naive method with two hierarchical loops
        Max profit with at most two transactions =
        MAX {max profit with one transaction and subarray price[0..i] +
            max profit with one transaction and aubarray price[i+1..n-1]  }
        i varies from 0 to n-1.
        Time complexity O(n^2)
    Way 2:
        First, Traverse price[] from right to left and update profit[i]
        such that profit[i] stores maximum profit achievable from one transaction in subarray price[i..n-1]
        Then, Traverse price[] from left to right and update profit[i]
        such that profit[i] stores maximum profit such that profit[i] contains maximum achievable profit from two transactions in subarray price[0..i].
        Finally, compare these two profit_array, find out the max profit
Reference:
    https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/
'''

def max_profit(price):
    num = len(price)

    # from right to left
    prof_r2l = [0] * num
    for i in range(num - 2, -1, -1):
        max_price = max(price[i + 1:])
        prof_r2l[i] = max(max_price - price[i], prof_r2l[i + 1])
    # from left to right
    prof_l2r = [0] * num
    for i in range(1, num):
        low_price = min(price[:i])
        prof_l2r[i] = max(price[i] - low_price, prof_l2r[i - 1])

    # merge two array, find max
    max_prof = 0
    for i, j in zip(prof_l2r, prof_r2l):
        prof_temp = i + j
        max_prof = max(max_prof, prof_temp)
    return max_prof


price = [90, 80, 70, 60, 50]
profit = max_profit(price)
print(profit)
