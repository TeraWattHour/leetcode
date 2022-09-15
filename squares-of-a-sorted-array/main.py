from typing import List


class Solution:
    def sort(self, nums: List[int], l: int, r: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        if l < r:
            pivot, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            self.sort(nums, l, ptr - 1)
            self.sort(nums, ptr + 1, r)
        return nums

    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [y**2 for y in nums]
        self.sort(nums, 0, len(nums) - 1)
        return nums


x = Solution()
y = x.sortedSquares([-4, -1, 0, 3, 10])
print(y)
