"""
Implement pow(x, n). 

x^n = x ^ n/2 * x ^ n/2
"""
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        """
        1. x == 0?
        2. n < 0?
        """
        if x == 0:
            return 1
        elif n < 0:
            n = -1 * n
            x = 1 / x

        result = 1
        factor = x
        while n > 0:
            if n % 2 == 1:
                result *= factor
            factor *= factor
            n /= 2

        return result
