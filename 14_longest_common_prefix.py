class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        longest_prefix = None
        for string in strs:
            if longest_prefix == None:
                longest_prefix = string
            else:
                min_len = min(len(longest_prefix), len(string))
                longest_prefix = longest_prefix[:min_len]
                for index in range(min_len):
                    if longest_prefix[index] != string[index]:
                        longest_prefix = longest_prefix[:index]
                        break

        return longest_prefix
