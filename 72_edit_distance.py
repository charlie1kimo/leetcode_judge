"""
Given two words word1 and word2, find the minimum number of steps required to
convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""


class Solution(object):
    """
    Idea:
        - DP (O(n^2)):
            Define D(i, j) = minimum edit distance between
                word1(0, 1) & word2(0, j)
            Define D(i, j) = min(
                                D(i - 1, j), --> delete
                                D(i, j - 1), --> insert
                                D(i - 1, j - 1) + 1 --> if replace
                            )
        - DP optimal (O(n)):
            space reduction on D(i - 1, j) <=> D(i, j -1) <=> D(i - 1, j - 1)
    """
    def minDistance_optimal(self, word1, word2):
        if word1 == word2:
            return 0

        if len(word1) == 0:
            return len(word2)

        if len(word2) == 0:
            return len(word1)

        m = len(word1)
        n = len(word2)
        min_distance = [0 for j in xrange(n + 1)]

        for j in xrange(1, n + 1):
            min_distance[j] = j

        for i in xrange(1, m + 1):
            prev = min_distance[0]
            min_distance[0] += 1
            for j in xrange(1, n + 1):
                temp = min_distance[j]
                min_distance[j] = min(
                    min_distance[j - 1] + 1,
                    min(
                        min_distance[j] + 1,
                        prev if word1[i - 1] == word2[j - 1] else prev + 1
                    )
                )
                prev = temp

        return min_distance[n]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0

        m = len(word1)
        n = len(word2)
        min_distance = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]

        for i in xrange(m + 1):
            min_distance[i][0] = i

        for j in xrange(n + 1):
            min_distance[0][j] = j

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                min_distance[i][j] = min(
                    min_distance[i - 1][j] + 1,
                    min(
                        min_distance[i][j - 1] + 1,
                        min_distance[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min_distance[i - 1][j - 1] + 1
                    )
                )

        return min_distance[m][n]
