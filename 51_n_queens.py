"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
import copy


class Solution(object):
    """
    Trial #1:
        - directly check each position using DFS
    Trial #2:
        - optimize it using one boolean 'is_valid array'
        - observing that for both (row-1, col-1) & (row-1, col+1) diagonal valid position check is 2*n - 1
        - 'is_valid_array' length = n + 2 * (2n - 1)
        - set (row+1, col+1) diagonal to False (placed queen @ (row, col)),
            is_valid_array index = n + row + col
        - set (row+1, col-1) diagonal to False (placed queen @ (row, col)),
            is_valid_array index = n + 2n - 1 + ((n-1) - row) + col = 4n - 2 - row + col

        - graph representation of diagnonal mappings:
        /**    | | |                / / /             \ \ \
          *    O O O               O O O               O O O
          *    | | |              / / / /             \ \ \ \
          *    O O O               O O O               O O O
          *    | | |              / / / /             \ \ \ \ 
          *    O O O               O O O               O O O
          *    | | |              / / /                 \ \ \
          *   3 columns        5 45° diagonals     5 135° diagonals    (when n is 3)
          */
    """
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #return self.solveNQueens_1(n)
        return self.solveNQueens_2(n)

    def solveNQueens_1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        retval = []
        board = ["." * n for i in range(n)]
        self.solveNQueensDFS(retval, board, 0, 0)
        return retval

    def solveNQueensDFS(self, results, board, row, queens_added):
        n = len(board)
        if row == n:
            results.append(copy.deepcopy(board))

        if queens_added > n:
            return

        for col in range(n):
            if self.isValid(board, row, col):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solveNQueensDFS(results, board, row+1, queens_added+1)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def isValid(self, board, row, col):
        n = len(board)
        # check if there's QUEEN before in the same column.
        for r in range(row):
            if board[r][col] == 'Q':
                return False

        # check if there's QUEEN before in the same row.
        for c in range(col):
            if board[row][c] == 'Q':
                return False

        # check (row-1, col-1) diagonal
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # check (row-1, col+1) diagonal
        r = row - 1
        c = col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

    def solveNQueens_2(self, n):
        retval = []
        board = ["." * n for i in range(n)]
        is_valid_array = [True for i in range((5 * n - 2))]
        self.solveNQueensDFS_optimized(retval, board, 0, 0, is_valid_array)
        return retval

    def solveNQueensDFS_optimized(self, results, board, row, queens_added, is_valid_array):
        n = len(board)
        if row == n:
            results.append(copy.deepcopy(board))

        if queens_added > n:
            return

        for col in range(n):
            if is_valid_array[col] and is_valid_array[n + row + col] and is_valid_array[4 * n - 2 - row + col]:
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                # set flag in the corresponding positions  in 'is_valid_array'
                is_valid_array[col] = is_valid_array[n + row + col] = is_valid_array[4 * n - 2 - row + col] = False
                self.solveNQueensDFS_optimized(results, board, row+1, queens_added+1, is_valid_array)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                # reset the flag
                is_valid_array[col] = is_valid_array[n + row + col] = is_valid_array[4 * n - 2 - row + col] = True
