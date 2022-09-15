class Solution:
    def reverseWord(self, word: str) -> str:
        agg = ""
        for x in reversed(range(0, len(word))):
            agg += word[x]
        return agg

    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed = [self.reverseWord(x) for x in words]
        agg = ""
        for x in range(0, len(reversed)):
            agg += reversed[x]
            if x != len(reversed) - 1:
                agg += " "
        return agg


x = Solution()
y = x.reverseWords("God Ding")
print(y)
