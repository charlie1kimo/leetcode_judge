"""
 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object):
    """
    Idea:
        go through every bit (32 bit), and shift up to compare.
        if dividend >= divisor, set that bit to 1.
        then dividend -= divisor left shift bits.
    """
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        INT_SIZE = 32

        if divisor == 0:
            return MAX_INT
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == MAX_INT:
                return MIN_INT
            if dividend == MIN_INT:
                return MAX_INT
            return -dividend

        is_negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend_long = abs(long(dividend))
        divisor_long = abs(long(divisor))

        res = 0
        for bit in reversed(range(INT_SIZE)):
            if dividend_long < divisor_long:
                break

            if dividend_long >= (divisor_long << bit):
                res |= 1 << bit
                dividend_long -= divisor_long << bit

        return -res if is_negative else res
