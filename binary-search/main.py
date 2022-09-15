from typing import List


class Solution:
    def getCenter(self, range: List[int]) -> int:
        return (range[0] + range[1]) // 2

    def search(self, nums: List[int], target: int) -> int:
        range = [0, len(nums) - 1]
        center = self.getCenter(range)
        while range[0] != range[1] and nums[center] != target:
            if range[0] + 1 == range[1]:
                center = range[0] + 1
                break
            if nums[center] > target:
                range = [range[0], center]
            elif nums[center] < target:
                range = [center, range[1]]
            center = self.getCenter(range)

        return center if nums[center] == target else -1


# [-1,0,3,5,9,12], 9
# [-1,0,3,5,9,12], 2

x = Solution()
y = x.search([5], -5)
print(y)
