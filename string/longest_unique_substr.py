'''
Problem:
    Given a string,
    find the length of the longest substring without repeating characters
Ways:
    scan the string from left to right
    record the length of the nearest unique sub-string
    update max length accordingly
Ref:
    https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
'''


def longest_unique_substr(string):
    # There are 128 characters in standard ASCII table
    # use char_sets to indicate the nearest location for char i
    char_sets = [-1] * 128
    # initialize the first character
    max_len = 1
    cur_len = 1
    char_sets[ord(string[0])] = 0
    number = len(string)

    for i in range(1, number):
        pre_ind = char_sets[ord(string[i])]
        # pre_ind == -1: if string[i] has not been observed
        # i-cur_len > pre_ind: string[i] is not in current unique substr
        if (pre_ind == -1) or (i-cur_len > pre_ind):
            cur_len += 1
        else:
            # string[i] is in current unique substr
            # we need to update cur_len
            # obviously, we should compare cur_len and max_len before discard cur_len
            max_len = max(max_len, cur_len)
            cur_len = i - pre_ind
        # document the location for string[i]
        char_sets[ord(string[i])] = i
    # consider last unique substr, update max_len if necessary
    max_len = max(max_len, cur_len)
    return max_len

string = "ABDEFGABEF"
length = longest_unique_substr(string)
print(length)
