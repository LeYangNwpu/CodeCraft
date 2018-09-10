def optim_fibonacci(first, second, n):
    print('dispose %d' % n)
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        return optim_fibonacci(second, first+second, n-1)

optim_fibonacci(1, 1, 8)
# for i in range(1, 9):
#     print(optim_fibonacci(1, 1, i))
