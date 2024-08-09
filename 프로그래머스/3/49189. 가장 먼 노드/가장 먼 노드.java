import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        for(int i=1; i<=n; i++) {
            graph.put(i, new ArrayList<>());
        }
        
        for(int[] e : edge) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        
        boolean[] visited = new boolean[n+1];
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{1,0});
        visited[1] = true;
        
        int count = 0;
        int maxdist = 0;
        while(!q.isEmpty()) {
            
            int[] cur = q.remove();
            if(maxdist < cur[1]) {
                maxdist = cur[1];
                count = 1;
            } else if(maxdist == cur[1]) {
                count++;
            }
            
            for(int next : graph.get(cur[0])) {
                if(visited[next]) continue;
                visited[next] = true;
                q.add(new int[]{next, cur[1] + 1});
            }
        }
        
        return count;
    }
}