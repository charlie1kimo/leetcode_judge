"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    For the return value, each inner list's elements must follow the lexicographic order.
    All inputs will be in lower-case.

Update (2015-08-09):
The signature of the function had been updated to return list<list<string>> instead of list<string>, as suggested here. If you still see your function signature return a list<string>, please click the reload button to reset your code definition. 
"""
class Solution(object):
    """
    idea:
        sort the str by character ordering. use that as a key to save a hashmap.
    time:
        O(n)
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # sort the strs first
        strs.sort()
        anagrams_map = {}
        for s in strs:
            key = "".join(sorted(s))
            if anagrams_map.has_key(key):
                anagrams_map[key].append(s)
            else:
                anagrams_map[key] = [s]

        ret = []
        for key in anagrams_map:
            ret.append(anagrams_map[key])

        return ret
