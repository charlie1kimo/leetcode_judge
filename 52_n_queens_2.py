"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""


class Solution(object):
    """
    Idea:
        - used the optimized solution from 51_n_queens.py

        * from 51_n_queens.py:
            - optimize it using one boolean 'is_valid array'
            - observing that for both (row-1, col-1) & (row-1, col+1) diagonal valid position check is 2*n - 1
            - 'is_valid_array' length = n + 2 * (2n - 1)
            - set (row+1, col+1) diagonal to False (placed queen @ (row, col)),
                is_valid_array index = n + row + col
            - set (row+1, col-1) diagonal to False (placed queen @ (row, col)),
                is_valid_array index = n + 2n - 1 + ((n-1) - row) + col = 4n - 2 - row + col
    """
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.total = 0
        is_valid_array = [True for i in xrange(5*n - 2)]
        self.totalNQueensDFS(0, n, is_valid_array)

        return self.total

    def totalNQueensDFS(self, row, n, is_valid_array):
        if row == n:
            self.total += 1
            return

        for col in xrange(n):
            if is_valid_array[col] and is_valid_array[n + row + col] and is_valid_array[4 * n - 2 - row + col]:
                is_valid_array[col] = is_valid_array[n + row + col] = is_valid_array[4 * n - 2 - row + col] = False
                self.totalNQueensDFS(row + 1, n, is_valid_array)
                is_valid_array[col] = is_valid_array[n + row + col] = is_valid_array[4 * n - 2 - row + col] = True
