"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
[
    [5 3 . . 7 . . . .],
    [6 . . 1 9 5 . . .],
    [. 9 8 . . . . 6 .],
    [8 . . . 6 . . . 3],
    [4 . . 8 . 3 . . 1],
    [7 . . . 2 . . . 6],
    [. 6 . . . . 2 8 .],
    [. . . 4 1 9 . . 5],
    [. . . . 8 . . 7 9],
]

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""


class Solution(object):
    """
    Idea:
        (1) separate checking:
            - check 3 booleans: row, col, box
            - have a set to keep track for each row, col, box checking
            - return 3 booleans AND together
            - Runtime: O(N^2), Space: O(1)
        (2) bitmap checking:
            - 3 int arrays for bitmaps
    """
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False

        l = len(board)
        row = [0 for i in xrange(l)]
        col = [0 for i in xrange(l)]
        box = [0 for i in xrange(l)]

        for i in xrange(l):
            for j in xrange(l):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if row[i] & 1 << num > 0:
                        # num exists in this row
                        return False
                    
                    if col[j] & 1 << num > 0:
                        # num exists this col
                        return False

                    box_ind = i / 3 * 3 + j / 3
                    if box[box_ind] & 1 << num > 0:
                        return False

                    row[i] |= 1 << num
                    col[j] |= 1 << num
                    box[box_ind] |= 1 << num

        return True

    def isValidSudoku_separate_check(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False

        row_valid = True
        col_valid = True
        box_valid = True

        l = len(board)
        # check row
        for j in xrange(l):
            nums = set()
            for i in xrange(l):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    if val in nums:
                        row_valid = False
                        break

                    nums.add(val)

            if not row_valid:
                break

        # check col
        for i in xrange(l):
            nums = set()
            for j in xrange(l):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    if val in nums:
                        col_valid = False
                        break

                    nums.add(val)

            if not col_valid:
                break

        # check box
        for a in xrange(0, l, 3):
            for b in xrange(0, l, 3):
                nums = set()
                for i in xrange(a, a + 3):
                    for j in xrange(b, b + 3):
                        if board[i][j] != '.':
                            val = int(board[i][j])
                            if val in nums:
                                box_valid = False
                                break

                            nums.add(val)

                    if not box_valid:
                        break
                if not box_valid:
                    break
            if not box_valid:
                break

        return row_valid and col_valid and box_valid
