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


def split(linked_list: LinkedList):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()

        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


### My working variant

# def merge(left: LinkedList, right: LinkedList):

#     l = LinkedList()  # noqa
#     i = 0
#     j = 0

#     while i < left.size() and j < right.size():

#         if left.searchByIndex(i).data < right.searchByIndex(j).data:

#             val = left.searchByIndex(i).data

#             l.append(val)
#             i = i + 1
#         else:

#             val = right.searchByIndex(j).data

#             l.append(val)
#             j = j + 1

#     while i < left.size():
#         val = left.searchByIndex(i).data
#         l.append(val)
#         i = i + 1

#     while j < right.size():
#         val = right.searchByIndex(j).data
#         l.append(val)
#         j = j + 1

#     return l


def merge(left: LinkedList, right: LinkedList):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    """

    # Create a new linked list that contains nodes from
    # merging left and right

    merged = LinkedList()

    # Add a fake head that is discarded later

    merged.add(0)

    # Set current to the head of the linked list

    current = merged.head

    # Obtain head nodes for left and right linked lists

    left_head = left.head
    right_head = right.head

    # Iterate over the left and right until we reach the tail node of either

    while left_head or right_head:

        # If the head node of left is None, we're past the tail
        # Add the node  from rightr to merged linked list

        if left_head is None:
            current.next_node = right_head

            # Call next on right to set loop condition to false

            right_head = right_head.next_node

        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list

        elif right_head is None:
            current.next_node = left_head

            # Call next on left to set loop condition to False

            left_head = left_head.next_node

        else:
            # Not at either tail node
            # Obtain node data to perform comparsion operations

            left_data = left_head.data
            right_data = right_head.data

            # if data on left is less than rigth, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # if data on left is greated than right, set current to right node
            else:
                current.next_node = right_head

                # Move right head to next_node

                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node
    # Discard fake head and set firsrt merged node as head

    head = merged.head.next_node
    merged.head = head
    return merged


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

l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)

sorted_linked_list = merge_sort(l)

print(sorted_linked_list)

# for i in range(0, 500):
#     a.add(random.randrange(0, 10000))

# print(merge_sort(a))
