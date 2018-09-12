'''
Problem:
    Given a string s, find the longest palindromic substring in s.
Way:
    use dynamic programming
    maintain a bool array of nxn, arr[i][j] indicates that string[i...j] is a palindromic substring
    thus, arr[i][j] = arr[i+1][j-1] and (string[i]==string[j])
    construct the array in bottom up manner
Ref:
    https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
'''

def longest_palindrominc_substring(string):
	num = len(string)
	P = [[False] * num for _ in range(num)]
	for i in range(num):
		P[i][i] = True
	len_max = - float('inf')
	i_min = None
	j_max = None
	for L in range(2, num+1):
		for i in range(num-L+1):
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

string = 'forgeeksskeegfor'
res_string = longest_palindrominc_substring(string)
print(res_string)

