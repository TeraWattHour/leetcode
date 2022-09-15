from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for x in range(0, len(s) // 2):
            s[x], s[len(s) - 1 - x] = s[len(s) - 1 - x], s[x]


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s.reverse()
