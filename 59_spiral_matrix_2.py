"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    """
    Idea:
        - Similar to 54_spiral_matrix
        - pre-allocate matrix, and fill it level by level
    """
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0 for j in xrange(n)] for i in xrange(n)]

        num = 1
        for lv in xrange(n / 2 + n % 2):
            for j in xrange(lv, n - lv):
                ret[lv][j] = num
                num += 1

            for i in xrange(lv + 1, n - lv):
                ret[i][n - 1 - lv] = num
                num += 1

            if n - 1 - lv == lv:
                break

            for j in reversed(xrange(lv, n - 1 - lv)):
                ret[n - 1 - lv][j] = num
                num += 1

            for i in reversed(xrange(lv + 1, n - 1 - lv)):
                ret[i][lv] = num
                num += 1

        return ret
