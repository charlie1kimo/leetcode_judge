"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
class Solution(object):
    """
    idea:
        binary search from [1, x]
    """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        while left <= right:
            mid = (left + right) / 2
            if pow(mid, 2) == x:
                return mid
            elif pow(mid, 2) > x:
                right = mid - 1
            else:
                left = mid + 1

        return right
