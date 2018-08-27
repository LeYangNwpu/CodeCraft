'''
Problem:
    Given an array of integers where each element represents the max number of steps that can be made forward from that element.
    Write a function to return the minimum number of jumps to reach the end of the array.
    If an element is 0, then cannot move through that element
Ways:
    Way 1: recursion solution
        for each point, try all reachable points, select the minimum one
    Way 2: record the minimum steps
        option 1: record the minimum steps from the current point to the end point
        option 2: record the minimum steps from the begin point to the current point
'''

def cal_min_jump(arr, loc, steps):
    length = len(arr)
    num_jump = arr[loc]
    if num_jump == 0:
        return float('inf')
    step_min = float('inf')
    for ijump in range(1, num_jump+1):
        loc_next = loc + ijump
        if loc_next >= length:
            step_min_temp = steps + 1
        else:
            step_min_temp = cal_min_jump(arr, loc_next, steps+1)
        step_min = min(step_min, step_min_temp)
    return step_min

def cal_min_jump_optim(arr):
    length = len(arr)
    doc_steps = [float('inf')] * length
    doc_steps[-1] = 1
    for iloc in range(length-2, -1, -1):
        num_jump = arr[iloc]
        if num_jump == 0:
            doc_steps[iloc] = float('inf')
            continue
        step_min = float('inf')
        for ijump in range(1, num_jump+1):
            loc_next = iloc + ijump
            if loc_next >= length:
                step_min_temp = 1
            else:
                step_min_temp = 1 + doc_steps[loc_next]
            step_min = min(step_min, step_min_temp)
        doc_steps[iloc] = step_min
    print('doc_steps', doc_steps)
    return doc_steps[0]


# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [1, 3, 6, 3, 2, 0, 6, 8, 9, 5]
jumps = cal_min_jump(arr, 0, 0)
# jumps = cal_min_jump_optim(arr)
print(jumps)

