import time

start_time = time.time()

s = "aacc"
t = "ccac"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check both lists are of same length, since we are only rearranging letters not adding or discarding

        if len(t) != len(s):
            return False

        s_dict_counter = {}
        t_dict_counter = {}

        for elem in s:
            if elem not in s_dict_counter:
                s_dict_counter[elem] = 1
            else:
                s_dict_counter[elem] = s_dict_counter[elem] + 1

        for elem in t:
            if elem not in t_dict_counter:
                t_dict_counter[elem] = 1
            else:
                t_dict_counter[elem] = t_dict_counter[elem] + 1

        for k in s_dict_counter:
            if k in t_dict_counter:
                if s_dict_counter[k] != t_dict_counter[k]:
                    return False
            else:
                return False

        return True


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
