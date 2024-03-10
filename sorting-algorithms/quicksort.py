import sys
import random
from load import load_numbers


# numbers = load_numbers(sys.argv[1])


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False

    return True


def partition(values, pivot, left_side, right_side):

    for i in range(1, len(values)):
        if values[i] <= pivot:
            left_side.append(values[i])  # O(n-1)
        elif values[i] > pivot:
            right_side.append(values[i])

    return left_side, right_side


def quicksort(values):

    if len(values) <= 1:  # O(1)
        return values

    left_side = []  # O(1)
    right_side = []  # O(1)
    join_result = []  # O(1)
    pivot = values[0]  # O(1)

    left_side, right_side = partition(values, pivot, left_side, right_side)  # O(n-1)

    sorted_left = quicksort(left_side)  # O(n-2)
    sorted_right = quicksort(right_side)

    # The order of operations is important. It's left + pivot + right, any other order messes up the sorting.
    join_result.extend(sorted_left)
    # append instead of extend because pivot is of type INT while extend works on type of list
    join_result.append(pivot)
    join_result.extend(sorted_right)

    return join_result


def random_list_input():
    h = []
    for i in range(0, 1000000):
        h.append(random.randrange(0, 1000000))
    return h


# sorted_numbers = quicksort(numbers)
# print(sorted_numbers)
# print(is_sorted(sorted_numbers))

h = random_list_input()
# print(h)
# sorted_h = quicksort(h)

# print(sorted_h)
# print(is_sorted(sorted_h))
