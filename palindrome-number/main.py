class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        st = str(x)
        for x in range(0, len(st)):
            if st[x] != st[len(st) - 1 - x]:
                return False
        return True


x = Solution()
y = x.isPalindrome(111)
print(y)
