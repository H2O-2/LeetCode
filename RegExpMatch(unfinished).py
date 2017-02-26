class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        regexp = p
        i = 0
        j = 0
        while j < len(regexp) and i < len(s):
            p_char = regexp[j]

            if j == len(regexp):
                break

            if p_char == '.':
                i += 1
                j += 1
                if j < len(regexp) and regexp[j] == '*':
                    j += 1
                    i -= 1
                    if j > len(regexp) - 1:
                        return True
                    while i < len(s):
                        if self.isMatch(s[i:], regexp[j:]):
                            return True
                        i += 1
                    return False
            elif p_char != '*':
                if (p_char != s[i] and j >= len(regexp) - 1) or (p_char != s[i] and regexp[j+1] != '*'):
                    return False
                elif j <= len(regexp) - 2 and regexp[j+1] == '*':
                    cur_char = regexp[j]
                    temp_j = j
                    while temp_j < len(regexp) and i < len(s):
                        if temp_j < len(regexp) - 1 and regexp[temp_j+1] == '*':
                            temp_j += 2
                        elif regexp[temp_j] == s[i]:
                            regexp = regexp[:temp_j] + regexp[(temp_j + 1):]
                            i += 1

                    while i <= len(s) - 1 and s[i] == cur_char:
                        i += 1

                    j += 2
                elif p_char == s[i]:
                    i += 1
                    j += 1

        if i < len(s):
            return False
        elif j < len(regexp):
            if (len(regexp) - j) % 2 != 0:
                return False
            while j < len(regexp):
                if regexp[j] == '*':
                    return False

                if regexp[j+1] == '*':
                    j += 2
                else:
                    return False

        return True


test = Solution()
print(test.isMatch("aaac", "ab*a*c*a"))

'''
    def check_exp(self, s, p, s_posn):
        if
'''