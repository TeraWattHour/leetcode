dividers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
mappings = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


class Solution:
    def intToRoman(self, num: int) -> str:
        divisions = []
        divider = 0
        while num > 0:
            if dividers[divider] > num:
                divider += 1
                continue
            times = num // dividers[divider]
            for _ in range(0, times):
                divisions.append(dividers[divider])

            num = num - (dividers[divider] * times)

        result = ""
        for x in range(0, len(divisions)):
            result += mappings[divisions[x]]
        return result


x = Solution()
y = x.intToRoman(1994)
print(y)
