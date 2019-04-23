class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        n = dividend_abs.bit_length()
        q = 0
        r = 0
        for i in range(n - 1, -1, -1):
            r = r << 1
            r = (r & ~1) | (dividend_abs >> i & 1)
            if r >= divisor_abs:
                r = r - divisor_abs
                q = (q & ~(1 << i)) | (1 << i)

        negative = True
        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            negative = False

        if q.bit_length() > 31 and not negative:
            return (1 << 31) - 1
        elif q.bit_length() > 31 and negative:
            return -(1 << 31)
        elif negative:
            return -q

        return q


sol = Solution()
print(sol.divide(100, -3))
