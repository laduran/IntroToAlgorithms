# Taken from the insertion sort algorithm in "Introduction to Algorithms" by Cormen, Lieserson, Rivest

# takes in a list of integers in possibly unsorted order
# returs the same list of integers in a sorted order
def insertion_sort(unsorted: list[int]) -> list[int]:
    for j in range(1, len(unsorted)):
        key = unsorted[j]
        i = j - 1
        while i >= 0 and unsorted[i] > key:
            unsorted[i+1] = unsorted[i]
            i -= 1
        unsorted[i+1] = key
    return unsorted

def main():
    unsorted = [5,2,4,6,1,3]
    sorted =insertion_sort(unsorted)
    print(sorted)

main()
