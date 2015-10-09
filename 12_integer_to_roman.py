class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        result = ""
        ROMAN_STR = [("I", "V"), ("X", "L"), ("C", "D"), ("M", "")]
        for i in reversed(xrange(0, 4)):
            div = pow(10, i)
            val = num / div
            num = num % div

            if val >= 5:
                if val == 9:
                    result += ROMAN_STR[i][0] + ROMAN_STR[i+1][0]
                elif val == 5:
                    result += ROMAN_STR[i][1]
                else:
                    result += ROMAN_STR[i][1] + ROMAN_STR[i][0] * (val - 5)
            else:
                if val == 4:
                    result += ROMAN_STR[i][0] + ROMAN_STR[i][1]
                else:
                    result += ROMAN_STR[i][0] * val

        return result
