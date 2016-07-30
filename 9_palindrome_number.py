"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""
class Solution:
    """
    idea:
        1. calculate num_of_digits
        2. find center, cut the digits in half
        3. decrement the integer by front part and end part.
        4. iterate till center
    """
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        num_digits = 0
        val = x
        while val > 0:
            val /= 10
            num_digits += 1
        
        # odd digits
        if num_digits % 2 == 1:
            digit_limit = (num_digits - 1) / 2
        # even digits
        else:
            digit_limit = num_digits / 2
        
        for i in xrange(digit_limit):
            front = x / (10 ** (num_digits-1-i))
            end = x % (10 ** (i+1)) / (10 ** i)
            
            if front != end:
                return False
            x -= (front * (10 ** (num_digits-1-i)))
            x -= (end * (10 ** i))
        
        return True
