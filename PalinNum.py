class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 10:
            return False

        num = x

        bit = -1
        bit_num = 1

        while bit < 0 or bit >= 10:
            bit = num // (10**bit_num)
            bit_num += 1

        i = 1
        j = 1
        while j < bit_num:
            left_bit = (num // (10**(bit_num - i))) % 10
            right_bit = (num % (10**i)) // (10**(i-1))
            if left_bit != right_bit:
                return False
            i += 1
            j += 2

        return True


test = Solution()
print(test.isPalindrome(12321))
