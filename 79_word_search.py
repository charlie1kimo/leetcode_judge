"""
 Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[str]
        :type word: str
        :rtype: bool
        """
        exist = False
        if board == None or len(board) == 0 or word == None or len(word) == 0:
            return exist

        # preprocess board
        for row in range(len(board)):
            board[row] = list(board[row])

        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] == word[0]:
                    board[r][c] = '#'
                    exist = exist or self.match(exist, board, word, 1, r, c)
                    board[r][c] = word[0]
        return exist

    def match(self, exist, board, word, curr_ind, row, col):
        # base case
        if curr_ind == len(word):
            return True

        if row - 1 >= 0:
            if board[row-1][col] == word[curr_ind]:
                board[row-1][col] = '#'
                exist = exist or self.match(exist, board, word, curr_ind+1, row-1, col)
                board[row-1][col] = word[curr_ind]
            else:
                exist = exist or False
        if row + 1 < len(board):
            if board[row+1][col] == word[curr_ind]:
                board[row+1][col] = '#'
                exist = exist or self.match(exist, board, word, curr_ind+1, row+1, col)
                board[row+1][col] = word[curr_ind]
            else:
                exist = exist or False
        if col - 1 >= 0:
            if board[row][col-1] == word[curr_ind]:
                board[row][col-1] = '#'
                exist = exist or self.match(exist, board, word, curr_ind+1, row, col-1)
                board[row][col-1] = word[curr_ind]
            else:
                exist = exist or False
        if col + 1 < len(board[0]):
            if board[row][col+1] == word[curr_ind]:
                board[row][col+1] = '#'
                exist = exist or self.match(exist, board, word, curr_ind+1, row, col+1)
                board[row][col+1] = word[curr_ind]
            else:
                exist = exist or False

        return exist


if __name__ == "__main__":
    sol = Solution()
    board = ["aa"]
    word = "aa"

    print sol.exist(board, word)
