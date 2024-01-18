
import time

start_time = time.time()

s = "aacc"
t = "ccac"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = 0
        for i in s:
            couint
        dict_t = {}
print(s)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # Check both lists are of same length, since we are only rearranging letters not adding or discarding

#         if len(t) != len(s):
#             return False
#         # Somehow we need to check that the elements in both lists are exactly the same, irespective of their position

#         # each list consists only of lowercase letters from a-z
#         # each list is unordered --- ordering helps to determine anagram. 
#         # If after ordering list1 = list2 means each element from s is a 1 to 1 to it's respective element in t. 
#         This includes duplicates as well



#         sorted_s = sorted(s) # O(nlogn) for the sorted() function and sort()
#         sorted_t = sorted(t)

#         print(sorted_s)
#         print(sorted_t)

#         if sorted_s == sorted_t: 
#             return True
#         else: 
#             return False

# solution = Solution()

# end_time = time.time()
# elapsed_time = end_time - start_time

# print(solution.isAnagram(s, t))
# elapsed_time = (end_time - start_time) * 1000
# print('Execution time:', elapsed_time, 'miliseconds')



