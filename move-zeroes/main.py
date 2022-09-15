from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0
        i = 0
        while x < len(nums) and i < len(nums):
            if nums[x] == 0:
                nums.pop(x)
                nums.append(0)
            else:
                x += 1
            i += 1


x = Solution()
y = x.moveZeroes([0, 0, 1])
