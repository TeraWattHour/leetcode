from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        c = nums[:]
        for x in range(0, len(nums)):
            toMove = (x + k) % len(nums)
            nums[toMove] = c[x]


x = Solution()
x.rotate([-1, -100, 3, 99], 2)
x.rotate([1, 2, 3, 4, 5, 6, 7], 3)
