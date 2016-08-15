"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution(object):
    """
    Idea:
        - DP
        - O(n^2) space:
            - standard DP approach
        - O(n) space:
            - each element is the min sum @ (m,n) position
    """
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        path_sum = [0 for i in xrange(m)]
        path_sum[0] = grid[0][0]
        for i in xrange(1, m):
            path_sum[i] = path_sum[i - 1] + grid[i][0]

        for j in xrange(1, n):
            path_sum[0] += grid[0][j]
            for i in xrange(1, m):
                path_sum[i] = min(path_sum[i - 1], path_sum[i]) + grid[i][j]

        return path_sum[m - 1]

    def minPathSum_n_square_space(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        path_sum = [[0 for j in xrange(n)] for i in xrange(m)]
        path_sum[0][0] = grid[0][0]
        for row in xrange(1, m):
            path_sum[row][0] = path_sum[row - 1][0] + grid[row][0]

        for col in xrange(1, n):
            path_sum[0][col] = path_sum[0][col - 1] + grid[0][col]

        for row in xrange(1, m):
            for col in xrange(1, n):
                path_sum[row][col] = min(path_sum[row - 1][col], path_sum[row][col - 1]) + grid[row][col]

        return path_sum[m - 1][n - 1]
