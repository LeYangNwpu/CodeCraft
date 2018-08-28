'''
Problem:
    Stock Buy Sell Multiple Times to Maximize Profit
Reference:
    https://www.geeksforgeeks.org/stock-buy-sell/
'''


def max_profit_infi(price):
    profit = 0
    increase_sets = []
    for i in range(1, len(price)):
        if price[i] > price[i-1]:
            if not len(increase_sets):
                increase_sets.append(price[i-1])
                increase_sets.append(price[i])
            else:
                increase_sets.append(price[i])
        else:
            if len(increase_sets):
                profit += increase_sets[-1] - increase_sets[0]
                increase_sets = []
    # dispose the last increase sets
    if len(increase_sets):
        profit += increase_sets[-1] - increase_sets[0]
    return profit


price = [100, 180, 260, 310, 40, 535, 695]
profit = max_profit_infi(price)
print(profit)
