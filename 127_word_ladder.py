"""
 Given two words (beginWord and endWord), and a dictionary,
 find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary

For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordDict: Set[str]
        :rtype: int
        """
        if wordDict == None or len(wordDict) == 0:
            return 0
        if beginWord not in wordDict or endWord not in wordDict:
            return 0

        # use queue on BFS traversal
        distance = 0
        queue = [beginWord]
        wordDict.remove(beginWord)
        while len(queue) > 0:
            distance += 1
            size = len(queue)
            for index in range(size):
                currWord = queue.pop(0)
                if currWord == endWord:
                    return distance

                # get new word based on currWord:
                for i in range(len(currWord)):
                    for ord_num in range(ord('a'), ord('z')+1):
                        char = chr(ord_num)
                        if char != currWord[i]:
                            newWord = currWord[:i] + char + currWord[i+1:]
                            if newWord in wordDict:
                                queue.append(newWord)
                                wordDict.remove(newWord)

        return 0
