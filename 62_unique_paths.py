"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

R . . . . . .
. . . . . . .
. . . . . . *

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""


class Solution(object):
    """
    Idea:
        - DP: (bottom up)
            - initialize path[m+1][n+1]
            - initialize path[m - 1][n] = 1 (one way to get to the end)
            - path[m][n] = path[m - 1][n] + path[m][n - 1]
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        path[m - 1][n] = 1
        for row in reversed(range(m)):
            for col in reversed(range(n)):
                path[row][col] = path[row + 1][col] + path[row][col + 1]

        return path[0][0]
