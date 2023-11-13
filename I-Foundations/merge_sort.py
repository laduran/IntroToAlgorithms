import math
# NOTE: detailed here: https://docs.python.org/3/whatsnew/2.2.html#pep-238-changing-the-division-operator

def merge(A, left, right):
    '''
    merges two lists into a single sorted list
    '''
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
    return A

def merge_sort(A):
    '''
    Divide and conquer. Split the list
    in two lists in the middle.
    merge the two lists
    '''
    if len(A) > 1:
        mid = len(A) // 2 # NOTE: uses the floor division operator // 
        left_half = A[:mid]
        right_half = A[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        return merge(A, left_half, right_half)

def main():
    unsorted = [9,2,4,6,1,3,7,5,8]
    sorted = merge_sort(unsorted)
    print(sorted)

main()