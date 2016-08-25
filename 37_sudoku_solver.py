"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # invalid board
        if board is None or len(board) != 9 or len(board[0]) != 9:
            return

        self.row = [0 for i in xrange(len(board))]
        self.col = [0 for i in xrange(len(board))]
        self.box = [0 for i in xrange(len(board))]

        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    k = i / 3 * 3 + j / 3

                    self.row[i] |= 1 << num
                    self.col[j] |= 1 << num
                    self.box[k] |= 1 << num

        for val in xrange(1, 10):
            if self.helper(board, 0, 0, 0, val):
                return

    def helper(self, board, i, j, k, num):
        # done with this row
        if j == 9:
            j = 0
            i += 1

        # reach bottom, done.
        if i == 9:
            return True

        # find next empty cell
        while board[i][j] != '.':
            j = (j + 1) % 9     # move to next column
            if j == 0:
                i += 1          # move to next row
            if i == 9:
                return True     # bottom, done.

        k = i / 3 * 3 + j / 3
        if self.isValid(i, j, k, num):
            # assign num to the position
            # python string is immutable, create new string.
            board[i][j] = str(num)
            self.row[i] |= 1 << num
            self.col[j] |= 1 << num
            self.box[k] |= 1 << num
        else:
            return False

        # try other position
        for val in xrange(1, 10):
            if self.helper(board, i, j + 1, k, val):
                return True

        # all combinations has failed, reverting
        # python string is immutable, create new string.
        board[i][j] = '.'
        self.row[i] ^= 1 << num
        self.col[j] ^= 1 << num
        self.box[k] ^= 1 << num
        return False

    def isValid(self, i, j, k, num):
        row = (self.row[i] & 1 << num) == 0
        col = (self.col[j] & 1 << num) == 0
        box = (self.box[k] & 1 << num) == 0

        return row and col and box
