"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    """
    Idea:
        - similar to 48_image_rotation.
        - ex:
            1  2  3  4  5  6
           16  17 18 19 20 7
           15  24 23 22 21 8
           14  13 12 11 10 9
        - observe that # of circle is m / 2 + m % 2
        - ex:
            1 1
            1 1
            1 1
            1 1
            1 1
    """
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        ret = []
        m = len(matrix)
        n = len(matrix[0])
        for k in xrange(min((m / 2 + m % 2), (n / 2 + n % 2))):
            for j in xrange(k, n - k):
                ret.append(matrix[k][j])

            for i in xrange(k + 1, m - k):
                ret.append(matrix[i][n - 1 - k])

            if m - 1 - k == k or n - 1 - k == k:
                break

            for j in reversed(xrange(k, n - 1 - k)):
                ret.append(matrix[m - 1 - k][j])

            for i in reversed(xrange(k + 1, m - 1 - k)):
                ret.append(matrix[i][k])

        return ret
