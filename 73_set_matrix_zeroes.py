"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place. 

Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        ideas:
        1. go through row 0 & col 0 to save 'row_zero' & 'col_zero'
        2. use row 0 & col 0 to save as flag for row 'i' & col 'j' == zero
        3. go through row 'i' & col 'j' from 1 - n and set zero using the flag from (2)
        4. set zeros if 'row_zero' & 'col_zero'

        space: O(1); time: O(mn)
        """
        if len(matrix) == 0:
            return

        row_zero = False
        col_zero = False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                row_zero = True
                break

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                col_zero = True
                break

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0

        if row_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        if col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
