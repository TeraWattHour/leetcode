from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in range(0, len(nums)):
            if nums[x] == target:
                return x

            if nums[x] < target:
                if x < len(nums) - 1:
                    if nums[x + 1] > target:
                        return x + 1
                else:
                    return x + 1
        return 0


x = Solution()
y = x.searchInsert([1, 3, 5, 6], 0)
print(y)
