from linked_list import LinkedList
import random


# My variant that is also working

# def split(lk_list: LinkedList):

#     current = lk_list.head

#     midpoint = lk_list.size() // 2

#     left = LinkedList()
#     right = LinkedList()

#     i = 0
#     while i < midpoint:
#         left.add(current.data)
#         current = current.next_node
#         i = i + 1

#     while i >= midpoint and i < lk_list.size():
#         right.add(current.data)
#         current = current.next_node
#         i = i + 1

#     return left, right


def merge(left: LinkedList, right: LinkedList):

    l = LinkedList()  # noqa
    i = 0
    j = 0

    while i < left.size() and j < right.size():

        if left.searchByIndex(i).data < right.searchByIndex(j).data:

            val = left.searchByIndex(i).data

            l.append(val)
            i = i + 1
        else:

            val = right.searchByIndex(j).data

            l.append(val)
            j = j + 1

    while i < left.size():
        val = left.searchByIndex(i).data
        l.append(val)
        i = i + 1

    while j < right.size():
        val = right.searchByIndex(j).data
        l.append(val)
        j = j + 1

    return l


def merge_sort(lk_list: LinkedList):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """

    if lk_list.size() == 1:
        return lk_list
    elif lk_list.head is None:
        return lk_list

    left_half, right_half = split(lk_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


a = LinkedList()
b = LinkedList()
c = LinkedList()
l = LinkedList()


# for i in range(0, 500):
#     a.add(random.randrange(0, 10000))

# print(merge_sort(a))
