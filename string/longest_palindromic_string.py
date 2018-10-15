'''
Problem:
    Given a string s, find the longest palindromic substring in s.
Way:
    1. use dynamic programming
      maintain a bool array of nxn, arr[i][j] indicates that string[i...j] is a palindromic substring
      thus, arr[i][j] = arr[i+1][j-1] and (string[i]==string[j])
      construct the array in bottom up manner
    2. search each place to find the longest palindromic string
      for a palindromic string s[i,...,j],
      the sub-string s[i+1,...,j-1] must be a palindromic
      thus we can loop through each place,
      find the palindromic sub-string with odd or even length
Ref:
    https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
    https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
'''

def longest_palindrominc_substring(string):
	num = len(string)
	P = [[False] * num for _ in range(num)]
	for i in range(num):
		P[i][i] = True
	len_max = - float('inf')
	i_min = None
	j_max = None
	# we maintain a two-dimension matrix, the first variable means the length of the sub-array
	for L in range(2, num+1):
		# the second variable means the start index of the sub-array
		for i in range(num-L+1):
			# the end index can be calculated as start_index+sub-array-length-1
			j = i + L - 1
			if j - i == 1:
				P[i][j] = (string[i]==string[j])
			else:
				P[i][j] = P[i+1][j-1] and (string[i]==string[j])
			if P[i][j]:
				if j-i+1 > len_max:
					len_max = j-i+1
					i_min = i
					j_max = j
	return string[i_min:j_max+1]


def is_palindromic(string):
	str_new = string[::-1]
	return string == str_new

def longest_palindromic_substr(string):
	num = len(string)
	rec_left = 0
	rec_right = 0
	longest_num = 0

	# odd length
	for cent in range(num):
		left = cent - 1
		right = cent + 1
		# notice: when we out the while loop, left and right value are not correct
		while (left >= 0) and (right < num) and (is_palindromic(string[left:right + 1])):
			left -= 1
			right += 1
		temp_length = right - left + 1
		if temp_length > longest_num:
			longest_num = temp_length
			rec_left = left + 1
			rec_right = right - 1
	# even length
	for cent in range(num):
		left = cent
		right = cent + 1
		while (left >= 0) and (right < num) and (is_palindromic(string[left:right + 1])):
			left -= 1
			right += 1
		temp_length = right - left + 1
		if temp_length > longest_num:
			longest_num = temp_length
			rec_left = left + 1
			rec_right = right - 1
	print('longest_palindromic', string[rec_left:rec_right+1])


string = 'forgeeksskeegfor'
# res_string = longest_palindrominc_substring(string)
# print(res_string)
longest_palindromic_substr(string)

