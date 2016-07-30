"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        row_array = ["" for r in range(numRows)]
        curr_row = 0
        direction = "add"
        for char in s:
            row_array[curr_row] += char
            if direction == "add":
                curr_row += 1
            else:
                curr_row -= 1

            if curr_row >= numRows or curr_row < 0:
                if direction == "add":
                    direction = "minus"
                    curr_row = numRows - 2
                else:
                    direction = "add"
                    curr_row = 1
                
        
        # print out
        print row_array
        return "".join(row_array)
