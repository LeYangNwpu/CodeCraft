def no_repeat(str_list):
    if len(str_list) == 1:
        return True
    char_set = [str_list[0]]
    for char in str_list[1:]:
        if char in char_set:
            return False
        else:
            char_set.append(char)
    return True


def longest_no_repeat_substr(str_list):
    num = len(str_list)
    Found = False
    longest_sub_strs = []
    for l in range(num - 1, 0, -1):
        for i in range(num - l):
            sub_str = str_list[i:i + l + 1]
            if no_repeat(sub_str):
                Found = True
                longest_sub_strs.append(sub_str)
        if Found:
            break
    return longest_sub_strs


string = 'ABDEFGABEF'
sub_strs = longest_no_repeat_substr(list(string))
print(sub_strs)

