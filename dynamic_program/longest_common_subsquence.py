'''
Problem:
	Given two sequences, find the length of longest subsequence present in both of them.
	A subsequence is a sequence that appears in the same relative order,
	but not necessarily contiguous.
Ways:
	Naive: check these two arrays from end to begin
		the transition function is:
		If last characters of both sequences match (or X[m-1] == Y[n-1]) then
			L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

		If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
			L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]) )
reference:
	https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
'''
def lcs(s1, s2):
	if len(s1) < 1 or len(s2) < 1:
		return 0
	if s1[-1] == s2[-1]:
		return 1+lcs(s1[:-1], s2[:-1])
	else:
		return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))

def lcs_store(s1, s2):
	m = len(s1)
	n = len(s2)
	arr = [[None] * (n+1) for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if (i == 0) or (j == 0):
				arr[i][j] = 0
			elif s1[i-1] == s2[j-1]:
				arr[i][j] = 1 + arr[i-1][j-1]
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])
	return arr

s1 = 'AGGTAB'
s2 = 'GXTXAYB'
# print(lcs(s1, s2))
arr = lcs_store(s1, s2)
print(arr[-1][-1])

