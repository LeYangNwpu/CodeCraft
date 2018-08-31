'''
Problem:
    Find minimum number of coins that make a given value
Ways:
    Dynamic programming
    1. f[i][v] means: only use the first i coins, make change v, the minimum number of coins
      f[i][v] = min{f[i-1][v], f[i-1][v-k*ci]+k}, 1 <= k <= v/ci
      we should maintain a 2D arr, for each location, loop through all possible k
    2. f[i] means: the minimum number of coins required
      we make value varies from 1 to n, use DP to choose minimum number of coins
    **can we solve this problem similar with "find weight for a balance", which could be faster
Reference:
    https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
'''

def mni_coins_num_optim(coins, value):
    coins.sort()
    inf = float('inf')
    arr = [inf] * (value+1)
    arr[0] = 0

    for ival in range(1, value+1):
        for jcoin in coins:
            if jcoin > ival:
                break
            sub_res = arr[ival-jcoin]
            if (sub_res != inf) and (sub_res+1<arr[ival]):
                arr[ival] = sub_res + 1
    # print(arr)
    return arr[value]

def mni_coins_num(coins, value):
    coins.sort()
    num_coin = len(coins)
    inf = float('inf')
    arr = [[inf] * (value+1) for i in range(num_coin+1)]
    for irow in range(num_coin+1):
        arr[irow][0] = 0

    for irow in range(1, num_coin+1):
        for jcol in range(1, value+1):
            coins_value = coins[irow-1]
            max_coin_num = int(jcol / coins_value)
            print('max_coin_num', max_coin_num)
            min_coins_k = inf
            for k in range(1, max_coin_num+1):
                min_coins_t = arr[irow-1][jcol-k*coins_value] + k
                print('min_coins_t', min_coins_t)
                min_coins_k = min(min_coins_k, min_coins_t)
            arr[irow][jcol] = min(min_coins_k, arr[irow-1][jcol])
    # for irow in range(num_coin+1):
    #     print(arr[irow])
    return arr[num_coin][value-1]



coins = [9, 6, 5, 1]
V = 11
# coins_num = mni_coins_num(coins, V)
coins_num = mni_coins_num_optim(coins, V)
print(coins_num)



