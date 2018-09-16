'''
Problem:
    Heap sort
Ways:
    Heap data structure:
      Big top heap, the value of root node is bigger than that of left node or right node
      That is, the largest value is at the root node
      Small top heap, the value of root node is smaller than that of left node or right node
      That is, the smallest value is at the root node
      We use big top heap
    Algorithm:
      in the heap, K_{i} >= K_{2i} and K_{i} >= K_{2i+1}, 1<=i<=int(n/2)
      Step1: construct a big top heap
      Step2: swap the root element with the last element in the heap
      Step3: adjust the element arr[1, ..., n-1] into a big top heap
      Step4: repeat step2 and step3 until i = 1
Notice:
     for the condition: K_{i} >= K_{2i} and K_{i} >= K_{2i+1}, 1<=i<=int(n/2)
     we must ensure the first element is stored in arr[1] rather than arr[0]
'''

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def heap_adjust(arr, s, m):
    temp = arr[s]
    j = 2 * s
    while j <= m:
        if (j < m) and (arr[j] < arr[j + 1]):
            j += 1
        if temp >= arr[j]:
            break
        arr[s] = arr[j]
        s = j
        j *= 2
    arr[s] = temp
    return arr

def heap_sort(arr):
    num = len(arr) - 1
    begin_point = int(num / 2)
    # construct the heap
    for i in range(begin_point, 0, -1):
        arr = heap_adjust(arr, i, num)
    print(arr)
    # heap sort
    for i in range(num, 1, -1):
        swap(arr, 1, i)
        heap_adjust(arr, 1, i-1)


arr = [0, 50, 10, 90, 30, 70, 40, 80, 60, 20]
heap_sort(arr)
print(arr)

