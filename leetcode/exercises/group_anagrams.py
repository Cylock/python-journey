from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # One condition would be to determine which elements are an anagram

        # - Iterate in some way through the input
        # - Determine anagram

        # Other condition is to group them and return a list of lists
        # What is the grouping condition?
        # - Add to corresponding group list
        trace = {}

        for i in range(len(strs)):  # For loop is O(n)

            sort_elem = "".join(sorted(strs[i]))  # O(k) - join method
            # klogk where k is length of the string - sorting method

            if sort_elem not in trace:  # searching keys in dictionary is O(1)
                trace[sort_elem] = [strs[i]]  # constant operation
            else:

                print("This is trace", trace)
                trace[sort_elem] = trace[sort_elem] + [strs[i]]  # O(1) + O(1)
                print("This is new trace")

        return list(trace.values())  # O (n)


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

sol = Solution()

print(sol.groupAnagrams(input_list))
