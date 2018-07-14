'''
Problem:
    Given a text txt[0..n-1] and a pattern pat[0..m-1] (n > m),
    write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
Requires:
    Use the KMP (Knuth Morris Pratt) Pattern Searching algorithm
Ways:
    The core idea of KMP algorithm is:
    whenever we detect a mismatch (after some matches),
    we already know some of the characters in the text of next window.
    We take advantage of this information to avoid matching the characters that we know will anyway match
Waiting:
    The implementation of calculating the next array in a elegant way is incorrect
'''

def get_next_array(arr):
	value = 1
	for ilen in range(1, len(arr)):
		fore_prex = arr[:ilen]
		back_prex = arr[len(arr)-ilen:]
		if fore_prex == back_prex:
			value = ilen + 1
	return value

def get_next(array):
	next_array = [0] * len(array)
	for iarr in range(1, len(array)):
		next_array[iarr] = get_next_array(array[:iarr])
	return next_array


# # the code for calculate next arrary is incorrect
# def get_next_new(array):
#     # num = len(array)
#     # arr_next = [0] * num
#     # c_len = 0
#     # i = 1
#     # while i:
#     #     if arr_next[i] == arr_next[c_len]:
#     #         c_len += 1
#     #         arr_next[i] = c_len
#     #         i += 1
#     #     else:
#     #         if c_len != 0:
#     #             c_len = arr_next[c_len - 1]
#     #         else:
#     #             arr_next[i] = 0
#     #             i += 1
#     # while i < num:
#     #     if c_len == 0 or arr_next[i] == arr_next[c_len]:
#     #         c_len += 1
#     #         arr_next[i] = c_len
#     #         i += 1
#     #     else:
#     #         c_len = arr_next[c_len - 1]
#     return arr_next

str_pri = 'ABABABCABABABCABABABC'
str_tar = 'ABABAC'
next_val = get_next(str_tar)
# next_val = get_next_new(str_tar)
print(next_val)

jtar = 0
ipri = 0
while ipri < len(str_pri):
    if str_pri[ipri] == str_tar[jtar]:
        if jtar == len(str_tar) - 1:
            print('match at the place %d : %d' % (ipri - len(str_tar) + 1, ipri))
            jtar = 0
        else:
            ipri += 1
            jtar += 1
            continue
    else:
        ipri += 1
        jtar = next_val[jtar]





