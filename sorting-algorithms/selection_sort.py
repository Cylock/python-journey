import random
from typing import List
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False

    return True


def selection_sort(values: List):  # T(n) = O(n) * O(n) = O(n^2)

    result = []

    while len(values) != 0:  # O(n)
        print("%-50s %-50s" % (values, result))
        min = values[0]

        minimum_index = 0
        for i in range(len(values)):
            if values[i] < min:  # O(n)
                min = values[i]
                minimum_index = i

        result.append(min)
        values.pop(minimum_index)
    return result


print(selection_sort(numbers))
