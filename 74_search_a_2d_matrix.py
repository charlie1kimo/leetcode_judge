"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""


class Solution(object):
    """
    Idea:
        (1) binary search row, then binary search col:
            - O(log(m) + log(n))
        (2) treat the matrix as a single array, calculate index, then binary search
            - operation of '%' (modular) might be expensive
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        # row index is (left - 1)
        row = left - 1
        if row < 0 or row >= len(matrix):
            return False

        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
