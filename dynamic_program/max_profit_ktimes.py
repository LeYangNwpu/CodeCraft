'''
Problem:
    Maximum profit by buying and selling a share at most k times
Ways:
    considering former problems, buy ans sell at 1 time, 2 times and multiple times
    this problem should be solved using dynamic programming:
    for all j in range [0, i-1]
	    profit[t][i] = max(profit[t][i-1], max(price[i] – price[j] + profit[t-1][j]))
Reference:
	https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/
'''

def max_profit_ktimes(price, k):
    num = len(price)
    arr = [[0] * num for i in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, num):
            prof_j = 0
            for t in range(j):
                prof_temp = price[j] - price[t] + arr[i-1][t]
                prof_j = max(prof_j, prof_temp)
            prof_j = max(arr[i][j-1], prof_j)
            arr[i][j] = prof_j
    print(arr)
    return arr[k][num-1]


price = [12, 14, 17, 10, 14, 13, 12, 15]
k = 3
profit = max_profit_ktimes(price, k)
print(profit)


