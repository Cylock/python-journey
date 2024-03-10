from typing import List

from test_data import big_ar


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

#         nums.sort()
#         print(nums)

#         if (len(nums) < 1) or (len(nums) > 10**5):
#             return 'Exceeded constraits'
#         # range function is not upper boundary inclusive,
#         # meanding a range(0,4) = [0,1,2,3]
#         for i in range(0, len(nums)-1):
#             if nums[i] > 10**9 or nums[i] < -10**9:
#                 return 'Exceeded constraits'

#             if nums[i] == nums[i+1]:
#                 return True         

#         return False


# ar = [1, 2, 3, 1]
# solution1 = Solution()

# print(solution1.containsDuplicate(big_ar))


# class Solution2:
#     def containsDuplicate(self, nums: List[int]) -> bool:

#         nums_set = set(nums)        

#         if (len(nums) < 1) or (len(nums) > 10**5):
#             return 'Exceeded constraits'
#         # range function is not upper boundary inclusive,
#         # meanding a range(0,4) = [0,1,2,3]
#         if len(nums) != len(nums_set):
#             return True
#         return False


# solution2 = Solution2()

# print(solution2.containsDuplicate(big_ar))


class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()
        
        for n in nums:
            
            if n in hashset:
                return True
            
            hashset.add(n)
        return False


solution3 = Solution3()

print(solution3.containsDuplicate(big_ar))


