from typing import List

# Working solution with time complexity of O(n)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return i, j


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            second_number = target - nums[i]
            sublist = nums[i + 1 :]
            if second_number in sublist:
                return i, nums.index(second_number, i + 1)

            # Tn = C1*n + C2*n + C3*n*k + C4*n*k + C5*n*n = n(C1+C2+C3*k+C4*n+C5*n)
            # Tn = n(C1+C2+C3*k)+n^2(C4+C5)


nums = [3, 2, 4]
target = 6

solution = Solution()
print(solution.twoSum(nums, target))
