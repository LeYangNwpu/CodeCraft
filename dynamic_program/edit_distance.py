'''
Problem:
    Given two strings str1 and str2 and below operations that can performed on str1.
    Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
    The available operations include: insert, remove, replace
Ways:
    The recursion method is a naive solution.
        If the last character is the same, no operation;
        else, try 3 available operations (insert, remove, replace) and select the minimal steps
    Notice, the stop condition should be carefully disposed
        Option 1:
            l_str1 = len(str1)
            l_str2 = len(str2)
            if l_str1 + l_str2 == 0:
                return 0
            if (l_str1 + l_str2 > 0) and (l_str1 * l_str2 == 0):
                return 10000
        Option 2:
            if len(str1) == 0:
                return len(str2)
            if len(str2) == 0:
                return len(str1)
        Option 2 is more elegant
    Optimize:
        there are overlaping sub-problem, which are computed again and again
        obviously, we can store result for the sub-problem
Ref:
    https://www.geeksforgeeks.org/edit-distance-dp-5/
'''

def edit_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)


    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    else:
        d_insert = edit_distance(str1, str2[:-1])
        d_remove = edit_distance(str1[:-1], str2)
        d_replace = edit_distance(str1[:-1], str2[:-1])
        return 1 + min(d_insert, d_remove, d_replace)


def edit_distance_optim(str1, str2):
    m = len(str1)
    n = len(str2)
    arr = [[None] * n for i in range(m)]
    for irow in range(m):
        for jcol in range(n):
            if irow == 0:
                arr[irow][jcol] = jcol
            elif jcol == 0:
                arr[irow][jcol] = irow
            elif str1[irow] == str2[jcol]:
                arr[irow][jcol] = arr[irow-1][jcol-1]
            else:
                d_insert = arr[irow][jcol-1]
                d_remove = arr[irow-1][jcol]
                d_replace = arr[irow-1][jcol-1]
                value = min(d_insert, d_remove, d_replace)
                arr[irow][jcol] = value + 1
    return arr, arr[m-1][n-1]


str1 = "sunday"
str2 = "saturday"
# min_operation = edit_distance(str1, str2)
# print(min_operation)
arr, min_operation = edit_distance_optim(str1, str2)
print(arr)
print(min_operation)



