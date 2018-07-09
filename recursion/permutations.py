'''
Problem:
    print the permutation of a string
Requires:
    sample: no repeated characters in the string
    hard: consider repeated characters and try to remove them
Ways:
    recursion, swap the characters and print them
    notice: for recursion, there must be some condition to stop
'''

def swap(s, i, j):
	temp = s[i]
	s[i] = s[j]
	s[j] = temp


def perm(s, left, right):
	if left == right:
		print(s)
	else:
		for i in range(left, right+1):
			swap(s, left, i)
			perm(s, left+1, right)
			swap(s, left, i)


s = ['a', 'b', 'c', 'd', 'e', 'f']
perm(s, 0, len(s)-1)



