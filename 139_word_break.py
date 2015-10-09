"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if s == None or len(s) == 0:
            return False

        if wordDict == None or len(wordDict) == 0:
            return False

        if s in wordDict:
            return True

        for index in range(1, len(s)+1):
            pre = s[:index]
            if pre in wordDict:
                post = s[index:]
                if self.wordBreak(post, wordDict):
                    return True

        return False
