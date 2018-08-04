'''
A dynamic programming problem contains two properties:
(1) Overlapping subproblems, we can store the results for each subproblem,
so as to reduce calculation
(2) Optimal substructure
'''

def fib(n, lookup):
    # base case
    if n == 0 or n == 1:
        return n
    if lookup[n] != None:
        return lookup[n]
    return fib(n-1, lookup) + fib(n-2, lookup)


def fib_tabulation(n, table):
    table[0] = 0
    table[1] = 1
    if n <= 1:
        return table[n]
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


n = 10
lookup = [None] * (n + 1)
result = fib(n, lookup)
print(result)

result = fib_tabulation(n, lookup)
print(result)



