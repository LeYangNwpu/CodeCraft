'''
Problem:
    print the permutation of a string
Requires:
    sample: no repeated characters in the string
    hard: consider list containing repeated characters and do not swap same characters
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

# we should judge whether we can swap word[begin] and word[terminal]
# only if word[begin, begin+1, ..., terminal-1] does not contain same char as word[terminal]
# we can make exchange
def is_swap(s, begin, terminal):
    for i in range(begin, terminal):
        if s[i] == s[terminal]:
            return False
    return True

def permutation(s, begin, terminal):
	if begin == terminal:
		print(s)
	else:
		i = begin
		while i <= terminal:
			if is_swap(s, begin, i):
				swap(s, begin, i)
				permutation(s, begin + 1, terminal)
				swap(s, begin, i)
				i += 1
			else:
				return

    # if (s is not None) and (begin <= terminal) and (begin >= 0) and (terminal <= len(s)-1):
    #     if begin == terminal:
    #         print(s)
    #     else:
    #         i = begin
    #         while i <= terminal:
    #             if is_swap(s, begin, i):
    #                 swap(s, begin, i)
    #                 permutation(s, begin+1, terminal)
    #                 swap(s, begin, i)
    #                 i += 1
    #             else:
    #                 return

s = list('abaab')
# perm(s, 0, len(s)-1)
permutation(s, 0, len(s)-1)



