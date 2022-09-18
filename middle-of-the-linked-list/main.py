import copy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lists = []
        while head:
            lists.append(head)
            head = head.next
        return lists[len(lists) // 2]


def check(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next


test1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))

x = Solution()
y = x.middleNode(test1)
check(y)
