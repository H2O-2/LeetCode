class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # check_1 = strs[0][0]

        if len(strs) <= 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        i = 0
        str_out = ""

        while i < len(strs[0]):
            check_1 = strs[0][i]
            for str_e in strs[1:]:
                if i >= len(str_e) or str_e[i] != check_1:
                    return str_out

            str_out += check_1
            i += 1
        return str_out

test = Solution()
print(test.longestCommonPrefix(["abc", "abd", "aba"]))
