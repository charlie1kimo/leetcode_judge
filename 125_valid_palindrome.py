"""
 Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. 
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None:
            return False
        if len(s) == 0:
            return True

        isPalindrome = True
        start = 0
        end = len(s)-1

        while start < end:
            if not self.isValidChars(s[start]):
                start += 1
                continue

            if not self.isValidChars(s[end]):
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                isPalindrome = False
                break

            start += 1
            end -= 1

        return isPalindrome


    def isValidChars(self, char):
        if (ord(char) >= 48 and ord(char) <= 57) or \
            (ord(char) >= 65 and ord(char) <= 90) or \
            (ord(char) >= 97 and ord(char) <= 122):
            return True

        return False
