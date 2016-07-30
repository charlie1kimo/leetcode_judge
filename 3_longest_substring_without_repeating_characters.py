"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        """
        idea:
            2 pointers. one start, one end. end traverse through string
            save a hashmap of indexes as end_pt goes.
            when end_pt hits a repeating_char, move the start to repeating_char + 1, update max
            
            # key point:
                - start_ind has to take MAX(). so it always starts at the later repeated index.
        """
        chars_map = dict()
        start_ind = 0
        end_ind = 0
        longest = 0
        while end_ind < len(s):
            curr_char = s[end_ind]
            if chars_map.has_key(curr_char):
                start_ind = max(start_ind, chars_map[curr_char] + 1)
            longest = max(longest, end_ind - start_ind + 1)
            chars_map[curr_char] = end_ind
            end_ind += 1
            
        return longest
