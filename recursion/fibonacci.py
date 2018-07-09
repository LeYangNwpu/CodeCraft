'''
Problem:
    suppose fibonacci series is: 1,1,2,3,5,8,... mathematically f(1) = 1, f(2) = 1, f(n) = f(n-1) + f(n-2)
    calculate the n th fibonacci
Requires:
    try different methods, such as, recursion, using array, loop, power of matrix, etc.
    try to achieve time complexity O(log n)
Ways:
    Simple implementation: recursion, using array, loop
    To achieve time complexity O(log n), we should combine recursion and power of matrix
    reference: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
'''
def fib(n):
    assert n > 0
    result = fibonacci(n)
    return result

def fibonacci(n):
	if n <= 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fib(3))

f1 = 1
f2 = 1
N = 20
n = 3
while n <= N:
    f = f1 + f2
    f1 = f2
    f2 = f
    n += 1
print(f)

