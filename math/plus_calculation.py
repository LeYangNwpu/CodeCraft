'''
Problem:
	Restrict we can only use addition operation, implement subtraction, multiplication and devision
'''
def neg_data(data):
    factor = -1 if data > 0 else 1
    count = 0
    while data:
        data += factor
        count += factor

    return count


def abs(a):
    if a >= 0:
        return a
    else:
        return neg_data(a)


def subtract(a, b):
    return a + neg_data(b)


def multiply(a, b):
    # make sure that a >= b
    if abs(a) < abs(b):
        a, b = b, a

    res = 0
    for _ in range(abs(b)):
        res += a
    if b >= 0:
        return res
    else:
        return neg_data(res)


def devide(a, b):
    # how to write assert?
    assert b != 0
    if (a >= 0 and b >= 0) or (a <= 0 and b <= 0):
        flag = True
    else:
        flag = False

    a = abs(a)
    b = abs(b)
    count = 0
    res_sum = b
    while res_sum <= a:
        count += 1
        res_sum += b


    if flag:
        return count
    else:
        return neg_data(count)


result = devide(-5, -3)
print(result)



