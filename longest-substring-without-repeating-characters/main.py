class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for x in range(0, len(s)):
            letters = []
            for y in range(0, len(s) - x):
                if (len(s) - x) + len(letters) <= result:
                    return result

                letter = s[x + y]
                if letters.count(letter) > 0:
                    break
                letters.append(letter)
            if len(letters) > result:
                result = len(letters)
        return result


x = Solution()
y = x.lengthOfLongestSubstring("abcabcbb")
print(y)
