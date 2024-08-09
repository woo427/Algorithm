import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int row = maps.length;
        int col = maps[0].length;
        boolean[][] visited = new boolean[row][col];
        
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        
        while(!q.isEmpty()) {
            int[] cur = q.remove();
            int cr = cur[0];
            int cc = cur[1];
            int dist = cur[2];
            
            int[] dr = {0, 0, -1, 1};
            int[] dc = {-1, 1, 0, 0};
            
            if(cr == row - 1 && cc == col - 1) {
                return dist;
            }
            
            for(int i=0; i<4; i++) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                
                if(nr>=0 && nr<row && nc>=0 && nc<col) {
                    if(maps[nr][nc] == 1) {
                        if(!visited[nr][nc]) {
                            visited[nr][nc] = true;
                            q.add(new int[]{nr, nc, dist+1});
                        }
                    }
                }
            }
        }
        
        return -1;
    }
}