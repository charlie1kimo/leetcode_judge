"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition. 
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s == None or len(s) == 0:
            return False

        index = 0
        nums = 0
        # valid sign, skipping
        if s[index] == '+' or s[index] == '-':
            index += 1

        while index < len(s) and ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
            index += 1
            nums += 1
        if index < len(s) and s[index] == '.':
            index += 1
        while index < len(s) and ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
            index += 1
            nums += 1

        # no digit before / after '.'
        if nums == 0:
            return False

        if index == len(s):
            return True
        elif index < len(s) and s[index] == 'e':
            index += 1
        else:
            return False

        # reset num after e
        nums = 0
        # valid sign, skipping
        if index < len(s) and (s[index] == '+' or s[index] == '-'):
            index += 1

        while index < len(s) and ord(s[index]) >= ord('0') and ord(s[index]) <= ord('9'):
            index += 1
            nums += 1

        # no digits after 'e'
        if nums == 0:
            return False

        if index == len(s):
            return True
        else:
            return False

