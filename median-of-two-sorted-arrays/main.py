class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        acc = nums1 + nums2
        acc.sort()
        m1 = self.getMedian(acc)

        return m1

    def getMedian(self, nums: list[int]) -> float:
        length = len(nums)
        center = int((length / 2) // 1)
        if length == 0:
            return -1
        if length % 2 == 0:
            second = center - 1
            return (nums[center] + nums[second]) / 2

        return nums[center]


x = Solution()
y = x.findMedianSortedArrays([1, 3], [2])
print(y)
