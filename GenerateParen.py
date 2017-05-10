class Solution(object):
    n = 0
    P_OPEN = "("
    P_CLOSE = ")"

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        p_stack = []
        open_num = close_num = n

        return self.p_recursion(open_num, close_num, p_stack, "", [])

    def p_recursion(self, open_num, close_num, p_stack, cur_str, generated_p):
        # assert open_num >= 0 and close_num >= 0

        if open_num == 0 and close_num == 0:
            generated_p.append(cur_str)
            return generated_p
        elif open_num == 0 and close_num != 0:
            result_str = cur_str
            while close_num != 0:
                result_str += self.P_CLOSE
                close_num -= 1
            generated_p.append(result_str)
            return generated_p

        if open_num > 0:
            p_stack_open = list(p_stack)
            p_stack_open.append(self.P_OPEN)
            self.p_recursion(open_num - 1, close_num, p_stack_open, cur_str + self.P_OPEN, generated_p)

        if len(p_stack) > 0:
            p_stack_close = list(p_stack)
            p_stack_close.pop()
            close_num -= 1
            cur_str += self.P_CLOSE
            self.p_recursion(open_num, close_num, p_stack_close, cur_str, generated_p)

        return generated_p


test = Solution()
print(test.generateParenthesis(1))
print(test.generateParenthesis(2))
print(test.generateParenthesis(3))
