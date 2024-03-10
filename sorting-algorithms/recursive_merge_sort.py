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
    """
    Merges two lists (arrays), sortim them in the process
    Returns a new merged list

    Runs in overall O(n) time

    """

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


def merge_sort(list):
    """
    Sorts a list in ascending order.
    Return a new sorted list.

    Divide: Find the midpoint of the list and dividte into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step

    Takes O(k * n log n) time

    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] <= list[1] and verify_sorted(list[1:])


a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 2, 3, 4, 5, 6, 7, 8]
c = [5, 4, 5, 6, 1]
d = [4, 2]
e = [4, 10, 10, 1]
f = [43, 12, 33, 50, 100]
g = [3, 5, 2, 4]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)  # noqa
print(verify_sorted(alist))
print(verify_sorted(l))

# print(merge_sort(a))
# print(merge_sort(b))
# print(merge_sort(c))
# print(merge_sort(d))
# print(merge_sort(e))
# print(merge_sort(f))
# print(merge_sort(g))
