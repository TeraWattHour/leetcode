from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            agg = nums[left] + nums[right]

            if agg == target:
                return [left + 1, right + 1]
            elif agg < target:
                left += 1
            else:
                right -= 1


x = Solution()
y = x.twoSum([2, 7, 11, 15], 9)
print(y)
