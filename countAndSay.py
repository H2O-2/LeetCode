class Solution:
    def countAndSay(self, n: int) -> str:
        return self.countAndSayStr("1", n - 1)

    def countAndSayStr(self, s: str, n: int) -> str:
        if n == 0:
            return s

        i = 0
        newStr = s
        while i < len(newStr):
            if i + 2 < len(newStr) and newStr[i] == newStr[i + 1] and newStr[i] == newStr[i + 2]:
                newStr = "".join((newStr[:i], "3" + newStr[i], newStr[i + 3:]))
            elif i + 1 < len(newStr) and newStr[i] == newStr[i + 1]:
                newStr = "".join((newStr[:i], "2" + newStr[i], newStr[i + 2:]))
            else:
                newStr = "".join((newStr[:i], "1" + newStr[i], newStr[i + 1:]))

            i += 2

        return self.countAndSayStr(newStr, n - 1)


sol = Solution()
print(sol.countAndSay(2))
