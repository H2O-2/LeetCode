class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        ptr_range = len(haystack) - len(needle) + 1
        for i in range(ptr_range):
            if haystack[i] == needle[0]:
                j = i + 1
                matched = True
                for char in needle[1:]:
                    if haystack[j] != char:
                        matched = False
                        break
                    else:
                        j += 1

                if matched:
                    return i

        return -1


test = Solution()
print(test.strStr("hello", "hello"))
