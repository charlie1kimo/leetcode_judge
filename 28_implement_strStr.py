"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer.
If you still see your function signature returns a char * or String, please click the reload button to reset your code definition. 
"""
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        for index in range(len(haystack)):
            sub_haystack = haystack[index:index+len(needle)]
            if sub_haystack == needle:
                return index

        if len(needle) == 0:
            return 0
        
        return -1
