'''
Problem:
    The Caesar Cipher technique is simply a type of substitution cipher
    Write a function to encoder and decoder the caesar cipher
Ways:
    Find the index for each char, shift it, then obtain the corresponding new char
    There are two ways to link a char with it index:
    1. construct two dictionary
    2. use the ord function
        new_char = chr((ord(char) + s - 65) % 26 + 65), or:
        new_char = chr((ord(char) + s - 97) % 26 + 97)
'''

def caesar_cipher(str_list, shift, is_encoder):
    # contrust the base situation
    # notice: this solution can only dispose upper characters
    index = range(26)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char_set = list(chars)
    dict_ind_char = dict(zip(index, char_set))
    dict_char_ind = dict(zip(char_set, index))

    if not is_encoder:
        shift *= -1

    str_new = []
    for astr in str_list:
        ind_ori = dict_char_ind[astr]
        ind_new = ind_ori + shift
        ind_search = ind_new % 26
        char_new = dict_ind_char[ind_search]
        str_new.append(char_new)

    return ''.join(str_new)


text = "ATTACKATONCE"
s = 4
string = caesar_cipher(list(text), s, is_encoder=True)
print(string)
string = caesar_cipher(list(text), s, is_encoder=False)
print(string)


