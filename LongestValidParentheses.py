class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0

        p_len = [0] * (len(s))

        if s[0] == '(' and s[1] == ')':
            p_len[1] = 2

        for i in range(2, len(s)):
            if s[i] == '(':
                continue
            elif s[i - 1] == '(' and s[i] == ')':
                p_len[i] = p_len[i - 2] + 2
            else:
                last_open = i - p_len[i - 1] - 1
                if last_open >= 0 and s[last_open] == '(':
                    p_len[i] = p_len[i - 1] + (p_len[last_open - 1] if last_open - 1 >= 0 else 0) + 2

        return max(p_len)


test = Solution()
print(test.longestValidParentheses(")()())()()("))
