import random


def split(list):
    """
    Divide the unsorted list at midpoint into  sublists
    Returns two sublists  - left and right

    Takes overal O( k * log n ) time, where k is the size of the slice ([index_1:index_2] <- slice)
    """

    midpoint = len(list) // 2

    left_half = list[:midpoint]
    right_half = list[midpoint:]

    return left_half, right_half


def merge(left, right):

    l = []  # noqa
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i + 1
        else:
            l.append(right[j])
            j = j + 1

    while i < len(left):
        l.append(left[i])
        i = i + 1

    while j < len(right):
        l.append(right[j])
        j = j + 1

    return l


def merge_sort(input_list):

    p = 2
    # while p <= len(input_list):

    #     print("For p = ", p, "--------------------------------")

    sorted_result = []

    for list_index in range(0, len(input_list), p):

        # print("A loop ----")
        # if p == 2:

        # slicing returns an array, and it seems you can slice out of bounds which python for convenience under the hood just replaces the out of bound index with len(n) # noqa
        # https://stackoverflow.com/questions/54613753/why-does-python-allow-out-of-range-slice-indexes-for-sequences
        slice_of_elements = input_list[list_index : list_index + p]  # noqa

        # else:
        #     slice_of_elements = next_input[list_index : list_index + p]

        # print("This is a slice:", slice_of_elements)
        left, right = split(slice_of_elements)
        # print("Left side:", left)
        # print("Right side:", right)
        sorted_chunk = merge(left, right)
        # print("Sorted_chunk:", sorted_chunk)
        sorted_result = merge(sorted_result, sorted_chunk)
        # print("Loop result:", sorted_result)

    # next_input = sorted_result

    # print("Input list:", input_list)
    # print("Sorted list:", sorted_result)
    return sorted_result


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] <= list[1] and verify_sorted(list[1:])


a = [55, 25, 10, 8, 100, 400, 15, 33]

b = [55, 25, 10, 8, 100, 400, 15, 33, 47, 89]

c = [10, 5, 6]

d = [4, 2]
e = [4, 10, 10, 1]
f = [43, 12, 33, 50, 100]
g = [3, 5, 2, 4]

h = []

for i in range(0, 500):
    h.append(random.randrange(0, 10000))


print(verify_sorted(merge_sort(a)))
print(verify_sorted(merge_sort(b)))
print(verify_sorted(merge_sort(c)))
print(verify_sorted(merge_sort(d)))
print(verify_sorted(merge_sort(e)))
print(verify_sorted(merge_sort(f)))
print(verify_sorted(merge_sort(g)))
print(verify_sorted(merge_sort(h)))
