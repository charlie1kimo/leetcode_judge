public class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        List<String> list = new ArrayList();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                String word = sb.toString();
                if (word.length() > 0) {
                    list.add(sb.toString());
                    sb = new StringBuilder();
                }
            }
            else {
                sb.append(s.charAt(i));
            }
        }
        list.add(sb.toString()); // last one
        
        sb = new StringBuilder();
        for (int i = list.size()-1; i >= 0; i--) {
            sb.append(list.get(i)+" ");
        }
        return sb.toString().trim();
    }
}
