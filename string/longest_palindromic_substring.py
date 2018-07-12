'''
Problem:
    Given a string s, find the longest palindromic substring in s.
Requires:
    if there exists multiple longest palindromics
    the code should be efficient
Way:
    for python, when check the palindromic, use s[::-1] to inverse the string
    loop from long to short
'''


def is_palindromic(s):
	s_inv = s[::-1]
	if s == s_inv:
		return True
	else:
		return False


def search_longest_palin(str_in):
    num_char = len(str_in)
    for len_tar in range(num_char, 0, -1):
        Flag = False
        result = []
        for i in range(0, num_char-len_tar+1):
            for j in range(i+len_tar, num_char):
                if is_palindromic(str_in[i:j]):
                    result.append(str_in[i:j])
                    Flag = True
        if Flag:
            return result
    return None


str_in = 'abcdeffedcabbcdeffedcb'
result = search_longest_palin(str_in)
print(result)



