'''
Problem:
    Given a text txt[0..n-1] and a pattern pat[0..m-1],
    write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]
Ways:
    using the KMP pattern matching algorithm
      first, calculate the next array, which can indicate the restart index for pattern string when mismatch
      then, scan the original string from left to right with index i, i never backdates
      we should change j properly during scan.
    Notice:
        for string and array tasks, we should carefully dispose the index for last element
Ref:
    https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
'''

def longest_same_str(astr):
    num = len(astr)
    len_max = 0
    # i indicates the length of sub-string, i = {1, ..., num-1}
    for i in range(1, num):
        fore_str = astr[:i]
        back_str = astr[-i:]
        if fore_str == back_str:
            len_max = i
    match = len_max + 1
    return match


def get_next(astr):
    num = len(astr)
    arr = [-1] * num
    arr[0] = 0
    arr[1] = 1
    # i indicates current next_array index, we should consider sub-string before i
    for i in range(2, num):
        arr[i] = longest_same_str(astr[:i])
    return arr


def pattern_match(astr, pstr):
	arr_next = get_next(pstr)
	i = 0
	j = 0
	len_astr = len(astr)
	len_pstr = len(pstr)
    # scan string from left to right
	while i < len_astr:
		if astr[i] == pstr[j]:
			i += 1
			j += 1
		if j == len_pstr:
			index = i - j
			print('pattern match at index %d' % index)
			j = arr_next[j-1]
		elif (i < len_astr) and (astr[i] != pstr[j]):
            # backdate j, try to find the match
			if j != 1:
				j = arr_next[j-1]
            # no match found, move to next character in the string
			else:
				i += 1


string = 'AABAACAADAABAABA'
pattern_string = 'AABA'
pattern_match(string, pattern_string)
