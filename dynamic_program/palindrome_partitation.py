'''
Problem:
    A partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome
    Determine the fewest cuts needed for palindrome partitioning of a given string
Ways:
    1. naive recursion
    2. C is an nxn matrix, C[i][j] means the min partition num for string S[i...j], use DP to calculate s[0][n-1]
        solve the problem in bottom-up manner
        if S[i...j] is palindrome: C[i][j] = 0
        else: C[i][j] = min{C[i][k] + C[k+1][j] + 1, k = i+1...j-1}
        in the loop, similar with matrix chain multiplication problem, use the sub-string length as a variable
    3. optimization:
        find all palindrome first, reduce time complicity into O(n^2)
Question:
    for a long string, which is palindrome itself, the above method would be in-efficient
    how about solve the problem in up-bottom manner?
'''

def is_palindrome(str_list):
    list_inv = str_list[::-1]
    if str_list == list_inv:
        return True
    else:
        return False

def min_part_rec(str_list):
    if len(str_list) == 1:
        return 0
    if is_palindrome(str_list):
        return 0
    num = len(str_list)
    num_cuts = float('inf')
    for k in range(1, num - 1):
        num_cut_temp = min_part_rec(str_list[:k]) + min_part_rec(str_list[k + 1:])
        num_cuts = min(num_cuts, num_cut_temp)
    return num_cuts + 1


def min_partitation_cuts(string):
    str_list = list(string)
    num = len(str_list)
    inf = float('inf')
    # we should maintain two matrix
    # matrix C for record min cuts
    C = [[inf] * num for _ in range(num)]
    # matrix P for record whether arr[i, ..., j] is palindrome
    P = [[False] * num for _ in range(num)]
    for i in range(num):
        C[i][i] = 0
        P[i][i] = True
    # string length
    for L in range(2, num + 1):
        # start index
        for i in range(num - L + 1):
            j = i + L - 1
            if j - i == 1:
                P[i][j] = (str_list[i] == str_list[j])
            else:
                P[i][j] = ((str_list[i] == str_list[j]) and P[i + 1][j - 1])

            if P[i][j]:
                C[i][j] = 0
            else:
                cuts_min = inf
                for k in range(i + 1, j):
                    cuts_temp = C[i][k] + C[k + 1][j]
                    cuts_min = min(cuts_min, cuts_temp)
                C[i][j] = cuts_min + 1
    return C[0][num - 1]

# # global cuts_mat
# inf = float('inf')
# def cal_value(cuts_mat, irow, jcol):
#     if cuts_mat[irow][jcol] != inf:
#         return cuts_mat
#     num_cuts = inf
#     for k in range(irow+1, jcol):
#         cuts_mat_t1 = cal_value(cuts_mat, irow, k)
#         cuts_mat_t2 = cal_value(cuts_mat, k+1, jcol)
#         num_cut_temp = cuts_mat_t1[irow][k] + cuts_mat_t2[k+1][jcol]
#         num_cuts = min(num_cuts, num_cut_temp)
#     cuts_mat[irow][jcol] = num_cuts + 1
#     return cuts_mat
#
# def min_partitation_cuts_inv(string):
#     str_list = list(string)
#     num = len(str_list)
#     if num == 1:
#         return 0
#     if is_palindrome(str_list):
#         return 0
#     # global cuts_mat
#     cuts_mat = [[inf] * num for i in range(num)]
#     for i in range(num):
#         cuts_mat[i][i] = 0
#     cuts_mat = cal_value(cuts_mat, 0, num-1)
#     number = cuts_mat[0][num-1]
#     return number


string = 'ababbbabbababa'
# number = min_part_rec(list(string))
number = min_partitation_cuts(string)
print(number)
