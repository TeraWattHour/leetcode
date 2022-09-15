# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = []
        while l1:
            d1.append(l1.val)
            l1 = l1.next
        d1.reverse()

        d2 = []
        while l2:
            d2.append(l2.val)
            l2 = l2.next
        d2.reverse()

        agg1 = 0
        agg2 = 0
        for x in range(0, len(d1)):
            ll = len(d1) - 1 - x
            agg1 += d1[x] * 10**ll

        for x in range(0, len(d2)):
            ll = len(d2) - 1 - x
            agg2 += d2[x] * 10**ll

        result = agg1 + agg2
        digits = []
        while result > 0:
            digits.append(result % 10)
            result = result // 10
        if len(digits) == 0:
            digits = [0]

        ll = None
        for x in reversed(range(0, len(digits))):
            ll = ListNode(digits[x], ll)

        return ll


# [2,4,9]
# [5,6,4,9]

# [1,0,9]
# [5,7,8]

# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
l1 = ListNode(1, ListNode(0, ListNode(9)))
l2 = ListNode(5, ListNode(7, ListNode(8)))
# l1 = ListNode(2, ListNode(4, ListNode(9)))
# l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
# l1 = ListNode(0)
# l2 = ListNode(0)

x = Solution()
y = x.addTwoNumbers(l1, l2)
