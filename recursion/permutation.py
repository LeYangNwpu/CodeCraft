def swap(s, begin, terminal):
	temp = s[begin]
	s[begin] = s[terminal]
	s[terminal] = temp

def is_swap(s, begin, terminal):
    for i in range(begin, terminal):
        if s[i] == s[terminal]:
            return False
    return True

def permutation(s, begin, terminal):
    if (s is not None) and (begin <= terminal) and (begin >= 0) and (terminal <= len(s)-1):
        if begin == terminal:
            print(s)
        else:
            i = begin
            while i <= terminal:
                if is_swap(s, begin, i):
                    swap(s, begin, i)
                    permutation(s, begin+1, terminal)
                    swap(s, begin, i)
                    i += 1
                else:
                    return
                # if begin == i or s[begin] != s[i]:
                #     swap(s, begin, i)
                #     permutation(s, begin+1, terminal)
                #     swap(s, begin, i)
                #     i += 1
                # else:
                #     return
permutation(list('abcd'), 0, 3)

