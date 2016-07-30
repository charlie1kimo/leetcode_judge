"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""


class Solution(object):
    """
    Idea:
        - DP (bottom up)
        - initialize path[m+1][n+1]
            - initialize path[m - 1][n] = 1 (one way to get to the end)
            - path[m][n] = path[m - 1][n] + path[m][n - 1] if no obstacle, else 0
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        path[m - 1][n] = 1

        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if obstacleGrid[row][col] == 0:
                    path[row][col] = path[row + 1][col] + path[row][col + 1]
                else:
                    path[row][col] = 0

        return path[0][0]
