"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""


class Solution(object):
    """
    Idea:
        - store a 'is_visited' array for each board position
        - iterate through each position, find an unvisit 'O' point to start
        - BFS on four directions
            - if directions contain other unvisit 'O', add to 'change_list'
                - add the coord to BFS queue.
            - if BFS search hit boundary, set a flag to not change the 'change_list'
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0 or \
                type(board[0]) is not list or len(board[0]) == 0:
            return

        m = len(board)
        n = len(board[0])
        is_visited = [[False for j in xrange(n)] for i in xrange(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in xrange(m):
            for j in xrange(n):
                # find BFS starting point
                if board[i][j] == 'O' and not is_visited[i][j]:
                    is_surrounded = True
                    change_pt_list = []
                    is_visited[i][j] = True
                    queue = []
                    queue.append((i, j))
                    # BFS
                    while len(queue) > 0:
                        change_pt = queue.pop(0)
                        change_pt_list.append(change_pt)
                        for direction in directions:
                            new_x = change_pt[0] + direction[0]
                            new_y = change_pt[1] + direction[1]

                            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                                is_surrounded = False
                            else:
                                if board[new_x][new_y] == 'O' and not is_visited[new_x][new_y]:
                                    queue.append((new_x, new_y))
                                # set is_visited to avoid inifite loop
                                is_visited[new_x][new_y] = True

                    # change the change_pt_list if it's surrounded
                    if is_surrounded:
                        for pt in change_pt_list:
                            x = pt[0]
                            y = pt[1]
                            board[x][y] = 'X'
