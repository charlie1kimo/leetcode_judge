public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<String> wordDict) {
        if (wordDict == null || wordDict.size() == 0) {
            return 0;
        }
        if (!wordDict.contains(beginWord) || !wordDict.contains(endWord)) {
            return 0;
        }
        
        int distance = 1;
        Queue<String> queue = new LinkedList();
        queue.add(beginWord);
        wordDict.remove(beginWord);
        while (queue.size() > 0) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String currWord = queue.poll();
                if (currWord.equals(endWord)) {
                    return distance;
                }
                
                // create new words and test see if they are in dict
                for (int j = 0; j < currWord.length(); j++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        char[] ch = currWord.toCharArray();
                        if (c == ch[j]) continue;
                        
                        ch[j] = c;
                        String newWord = new String(ch);
                        if (wordDict.contains(newWord)) {
                            queue.add(newWord);
                            wordDict.remove(newWord);
                        }
                    }
                }
            }
            distance++;
        }
        return 0;
    }
}