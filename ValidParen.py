class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_p = ['(', '[', '{']
        close_p = [')', ']', '}']

        p_stack = []

        for p_char in s:
            if p_char in open_p:
                p_stack.append(p_char)
            elif p_char in close_p:
                if len(p_stack) == 0:
                    return False
                elif close_p.index(p_char) == open_p.index(p_stack[len(p_stack) - 1]):
                    p_stack.pop()
                else:
                    return False

        if len(p_stack) == 0:
            return True

        return False

test = Solution()
print(test.isValid("]"))

