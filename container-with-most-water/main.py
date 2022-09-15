from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            if height[i] < height[j]:
                maxArea = max(maxArea, (height[i]) * abs(j - i))
                i += 1
            else:
                maxArea = max(maxArea, (height[j]) * abs(j - i))
                j -= 1

        return maxArea


x = Solution()
y = x.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(y)
