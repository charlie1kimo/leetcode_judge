class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        ROMAN_CHARS = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        index = 0
        while index < len(s):
            val = ROMAN_CHARS[s[index]]
            next_val = 0
            if index+1 < len(s):
                next_val = ROMAN_CHARS[s[index+1]]

            if next_val > val:
                val = next_val - val
                index += 1

            num += val
            index += 1

        return num
