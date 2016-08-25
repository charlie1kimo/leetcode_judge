"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


class Solution(object):
    """
    Idea:
        - In place rotation.
        - rotate the image level-by-level like this (int indicates level #)
        1 1 1 1 1 1 1 1
        1 2 2 2 2 2 2 1
        1 2 3 3 3 3 2 1
        1 2 3 4 4 3 2 1
        1 2 3 4 4 3 2 1
        1 2 3 3 3 3 2 1
        1 2 2 2 2 2 2 1
        1 1 1 1 1 1 1 1
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        n = len(matrix)
        for i in xrange(n / 2):
            for j in xrange(i, n - 1 - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp

        return
