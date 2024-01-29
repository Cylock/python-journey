

a = [1,2,3,4,5,6,7]
b = [1,2,3,4,5,6,7,8]
c = [5,4,5,6,1]
d = [4,2]
e = [4,4,4,1]
f = [43,12,33,50,100]
g = [3,5,2,4]


def split(list):
    
    midpoint = len(list)//2
    
    left_half = list[:midpoint]
    right_half = list[midpoint:]
    
    return left_half, right_half


def merge(left, right):

    """
    Merges two lists (arrays), sortim them in the process
    Returns a new merged list
    """
    
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i + 1
        else:
            

def merge_sort(list):
    """
    Sorts a list in ascending order.
    Return a new sorted list.
    
    Divide: Find the midpoint of the list and dividte into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)


# print(merge_sort(a))
# print(merge_sort(b))
# print(merge_sort(c))
# print(merge_sort(d))
# print(merge_sort(e))
# print(merge_sort(f))
# print(merge_sort(g))