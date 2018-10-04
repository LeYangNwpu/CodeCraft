'''
Problem:
    Check for balanced parentheses in an expression
Ways:
    1. stack
      implement stack via list with append and pop operations
      for the opening paren '(', '[', '{', push it to stack
      for the closing paren ')', ']', '}', pop a paren from the stack, and check the match
    2. optimize space
      search the closing paren, the former paren should match with this paren
      then remove these two parens
      continue until expression is empty
    3. recursion
      for the first paren, find it matching closing paren
      then recursively check the remaining two expressions
Ref:
    https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
    https://www.geeksforgeeks.org/check-balanced-parentheses-expression-o1-space/
    https://www.geeksforgeeks.org/minimum-number-of-bracket-reversals-needed-to-make-an-expression-balanced/
'''

def inverse_char(cha):
    if cha == ')':
        return '('
    elif cha == ']':
        return '['
    else:
        return '{'

def is_balanced_bracket(exp):
    start = ['(', '[', '{']
    end = [')',']','}']
    data = list()
    for cha in exp:
        if cha in start:
            data.append(cha)
        elif cha in end:
            if len(data) > 0:
                cha_p = data.pop()
                if cha_p != inverse_char(cha):
                    print('unblanced')
                    return False
            else:
                print('unblanced')
                return False
        else:
            print('illeage char')
    if len(data) != 0:
        print('unblanced')
        return False
    return True


def is_balanced_opt_space(exp):
    if len(exp) % 2 == 1:
        print('unbalanced')
        return False
    closing = [')', ']', '}']
    while exp:
        for i, cha in enumerate(exp):
            if cha in closing:
                break
        print(i, cha)
        if i == 0:
            print('unbalanced')
            return False
        cha_m = exp[i-1]
        if inverse_char(cha) == cha_m:
            exp = exp[:i - 1] + exp[i + 1:]
        else:
            print('unbalanced')
            return False

    return True

exp = '))(('
print(is_balanced_opt_space(exp))
