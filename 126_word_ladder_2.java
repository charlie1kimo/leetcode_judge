public class Solution {
    public List<List<String>> findLadders(String start, String end, Set<String> dict) {
        List<List<String>> ret = new ArrayList();
        if (dict == null || dict.isEmpty()) {
            return ret;
        }
        if (!dict.contains(start) || !dict.contains(end)) {
            return ret;
        }
        
        Map<String, List<String>> map = new HashMap();
        Map<String, Integer> distances = new HashMap();
        List<String> path = new ArrayList();
        bfs(map, distances, start, end, dict);
        dfs(ret, path, end, start, map, distances);
        return ret;
    }
    
    // bfs map for child has List<String> parent.
    public static void bfs(Map<String, List<String>> map, Map<String, Integer> distances,
                        String start, String end, Set<String> dict) {
        Queue<String> queue = new LinkedList();
        queue.add(start);
        distances.put(start, 0);
        for (String str : dict) {
            map.put(str, new ArrayList<String>());
        }
        
        while (!queue.isEmpty()) {
            String word = queue.poll();
            List<String> neighbors = expand(word, dict);
            for (String neighbor : neighbors) {
                map.get(neighbor).add(word);
                if (!distances.containsKey(neighbor)) {
                    distances.put(neighbor, distances.get(word)+1);
                    queue.add(neighbor);
                }
            }
        }
    }
    
    public static List<String> expand(String word, Set<String> dict) {
        List<String> neighbors = new ArrayList();
        for (int i = 0; i < word.length(); i++) {
            for (char c = 'a'; c <= 'z'; c++) {
                char[] ch = word.toCharArray();
                if (ch[i] == c) continue;
                ch[i] = c;
                String newWord = new String(ch);
                if (dict.contains(newWord)) {
                    neighbors.add(newWord);
                }
            }
        }
        return neighbors;
    }
    
    // trace from end -> start
    public static void dfs(List<List<String>> ret, List<String> path, String word,
                        String start, Map<String, List<String>> map, Map<String, Integer> distances) {
        if (word.equals(start)) {
            path.add(0, word);
            ret.add(new ArrayList<String>(path));
            path.remove(0);
            return;
        }
        
        for (String neighbor : map.get(word)) {
            if (distances.containsKey(neighbor) &&
                distances.get(word) == distances.get(neighbor) + 1) { // backward trace.
                path.add(0, word);  // add current word
                dfs(ret, path, neighbor, start, map, distances);  // dfs next round
                path.remove(0);
            }
        }
    }
}