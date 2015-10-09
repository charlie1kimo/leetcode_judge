"""
 Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary

For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:

    All words have the same length.
    All words contain only lowercase alphabetic characters.
"""
class Solution(object):
    def findLadders(self, start, end, dict):
        """
        :type start: str
        :type end: str
        :type dict: Set[str]
        :rtype: List[List[int]]

        idea:
            1. BFS: (stop @ end, shortest path)
                - build word distance from start (keep out the loop)
                - build word's neighbor words list
            2. DFS:
                - drill down from start. go through neighbor list
                - save the path and return
        """
        if dict == None or len(dict) == 0:
            return []

        if not start in dict or not end in dict:
            return []

        words_map, dist_map = self.bfs(start, end, dict)
        ret = []
        self.dfs(ret, [], start, end, words_map, dist_map)
        return ret

    def bfs(self, start, end, dict):
        done = False
        distance = 0
        words_map = {}
        dist_map = {}
        queue = [start]
        while len(queue) > 0 and not done:
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if word == end:
                    done = True

                neighbors = self.expand(word, dict)
                words_map[word] = neighbors
                dist_map[word] = distance
                queue += neighbors

            distance += 1

        return words_map, dist_map

    def expand(self, word, dict):
        neighbors = []
        chars = 'abcdefghijklmnopqrstwvxyz'
        for index in range(len(word)):
            for c in chars:
                if word[index] != c:
                    new_word = word[:index] + c + word[index+1:]
                    if new_word in dict:
                        neighbors.append(new_word)

        return neighbors

    def dfs(self, ret, path, word, end, words_map, dist_map):
        if word == end:
            path.append(word)
            ret.append(list(path))
            path.pop()
            return

        word_distance = dist_map[word]
        for neighbor in words_map[word]:
            neighbor_distance = dist_map[neighbor]
            if word_distance + 1 == neighbor_distance:
                path.append(word)
                self.dfs(ret, path, neighbor, end, words_map, dist_map)
                path.pop()



if __name__ == "__main__":
    start = "a"
    end = "c"
    dict = set(["a", "b", "c"])

    sol = Solution()
    print sol.findLadders(start, end, dict)

