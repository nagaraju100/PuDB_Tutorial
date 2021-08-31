import random
import math
#Initial Size
ARRAYSIZE = 8

#Swaps the two numbers
def swap(array, x, y):
    tmp = array[x]
    array[x] = array[y]
    array[y] = tmp

# Compare two numbers
def compare_lt(array, x, y):
    return array[x] < array[y]

# Sort the array using bubble sort
def bubblesort(array, start, stop):

    for _ in range(math.ceil((len(array)))):
        for x in range(len(array) - 1):
            if compare_lt(array, x, x + 1):
                swap(array, x, x + 1)

# Sort the array using quick sort
def quicksort(array, start, stop):
    if stop - start < 2:
        return True
    import pudb
    pudb.set_trace()  # breakpoint  //

    larger_index = stop - 2
    smaller_index = start
    # the "whole" starts where the pivot does
    pivot = array[stop - 1]
    hole = stop - 1

    while larger_index + 1 > smaller_index:
        if compare_lt(array, stop - 1, larger_index):
            # good case, this is the right side
            # just shift the whole and continue!
            array[hole] = array[larger_index]
            larger_index -= 1
            hole -= 1
        else:
            # gotta put it on the other side
            swap(array, larger_index, smaller_index)
            smaller_index += 1

    array[hole] = pivot

    quicksort(array, start, hole)
    quicksort(array, hole + 1, stop)


def test_sorts(sortfn):
    random.seed('ladyred')
    array = [random.randrange(ARRAYSIZE) for x in range(ARRAYSIZE)]
    sortfn(array, 0, len(array))
    for x, y in zip(array, array[1:]):
        assert x < y


def main():
    test_sorts(quicksort)
    test_sorts(bubblesort)


if __name__ == '__main__':
    main()