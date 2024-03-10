from typing import List


a = [5, 1, 2, 54, 6]


def recursive_sum(sublist: List):

    result_sum = 0

    if len(sublist) == 1:
        return sublist[0]
    remaining = recursive_sum(sublist[1:])
    result_sum = sublist[0] + remaining
    return result_sum


def verify_sum(list):
    if sum(list) == recursive_sum(list):
        return True
    else:
        return False


print(recursive_sum(a))
