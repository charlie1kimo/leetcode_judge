"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import sys
MAX_INT = 2147483647        # 32 bit int
MIN_INT = -1 * MAX_INT - 1

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        is_negative = False
        string = str(x)
        if x < 0:
            string = string[1:]
            is_negative = True

        new_int = 0
        for index, digit in enumerate(string):
            val = int(digit) * 10**index
            if val + new_int > MAX_INT or val + new_int < MIN_INT:
                return 0
            new_int += val
            
        if is_negative:
            new_int *= -1
        
        return new_int
