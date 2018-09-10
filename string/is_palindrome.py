def is_palindrome(s):
    # consider the stop condition
    start = 0
    end = len(s) - 1
    while end > start:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

# def is_palindrome(s):
#     # consider the stop condition
#     if len(s) <= 1:
#         return True
#     if s[0] != s[len(s)-1]:
#         return False
#     else:
#         return is_palindrome(s[1:-1])

print(is_palindrome('abdcdcba'))
