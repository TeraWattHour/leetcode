# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


from random import random
from typing import List


def isBadVersion(n: int) -> bool:
    return n == 100


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1
        r = [1, n]
        while r[1] - r[0] > 1:
            m = (r[0] + r[1]) // 2
            if isBadVersion(m):
                r = [r[0], m]
            else:
                r = [m, r[1]]
        return r[1]


x = Solution()
y = x.firstBadVersion(100)
print(y)
