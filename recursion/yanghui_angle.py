def get_value(x, y):
    print('process (%d, %d)' % (x, y))
    if (y < 0) or (x == y):
        return 1
    else:
        return get_value(x-1, y-1) + get_value(x-1,y)
print(get_value(100, 50))



