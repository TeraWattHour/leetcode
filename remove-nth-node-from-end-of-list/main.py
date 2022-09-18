from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        nodes.pop(len(nodes) - n)
        res = None
        for x in reversed(range(0, len(nodes))):
            res = ListNode(nodes[x], res)
        return res


test1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


def check(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next


x = Solution()
y = x.removeNthFromEnd(test1, 1)
# check(y)
