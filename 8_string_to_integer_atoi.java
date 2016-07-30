/*
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
*/
public class Solution {
    public int myAtoi(String str) {
        try {
            str = preProcess(str);
        }
        catch (Exception e) {
            return 0;
        }
        if (str.length() == 0) { return 0; }
        
        char sign = str.charAt(0);
        if (sign ==  '+' || sign == '-') {
            str = str.substring(1);
        }
        else {
            sign = '+';
        }
        int result = 0;
        for (int i = 0; i < str.length(); i++) {
            double val = ((int)str.charAt(i) - (int)'0') * Math.pow(10, str.length()-1-i);
            if ((val + result) > Integer.MAX_VALUE) {
                int retval = (sign == '+') ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                return retval;
            }
            else if ((val + result) == Integer.MAX_VALUE && sign == '-') {
                return -1 * Integer.MAX_VALUE;
            }
            result += val;
        }
        if (sign == '-') {
            result *= -1;
        }
        return result;
    }
    
    private static String preProcess(String str) {
        str = str.trim();
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < str.length(); i++) {
            char character = str.charAt(i);
            if (character >= '0' && character <= '9') {
                sb.append(character);
            }
            else if (i == 0 && (character == '+' || character == '-')) {
                sb.append(character);
            }
            else {
                return sb.toString();
            }
        }
        return sb.toString();
    }
}
