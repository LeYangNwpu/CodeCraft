'''
Problem:
    Given n non-negative integers a_1, a_2, ..., a_n
    where each represents a point at coordinate  (i, a_i) .
    ‘ n ‘ vertical lines are drawn such that the two endpoints of line i is
    at  (i, a_i)  and (i, 0). Find two lines,
    which together with x-axis forms a container,
    such that the container contains the most water.
Ways:
    Decompose this problem into a simpler one:
    which is better, A or B?
    A: current state, B: adjust the left or right point with one step
Ref:
    https://www.geeksforgeeks.org/container-with-most-water/
'''
# def most_water(arr, left, right):
# 	if left >=right:
# 		return 0
# 	v_left = arr[left]
# 	v_right = arr[right]
# 	base_water = (right - left) * min(v_left, v_right)
# 	if v_left < v_right:
# 		change_water = most_water(arr, left+1, right)
# 	else:
# 		change_water = most_water(arr, left, right-1)
# 	return max(base_water, change_water)

def most_water_optim(arr):
    left = 0
    right = len(arr)-1
    water = 0
    while left < right:
        water_temp = (right - left) * min(arr[left], arr[right])
        water = max(water, water_temp)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return water

height = [1, 5, 4, 3]
# water = most_water(height, 0, len(height)-1)
water = most_water_optim(height)
print(water)
