import java.util.*;

class Solution {
    //시간을 분단위로 변환
    public int ttm(String time) {
        String[] hm = time.split(":");
        int h = Integer.parseInt(hm[0]);
        int m = Integer.parseInt(hm[1]);
        return h * 60 + m;
    }
    
    public int solution(String[][] book_time) {
        int answer = 0;
        
        List<int[]> rooms = new ArrayList<>();
        for(String[] times : book_time) {
            String start = times[0];
            String end = times[1];
            rooms.add(new int[]{ttm(start), 1});
            rooms.add(new int[]{ttm(end)+10, -1});
        }
        
        Collections.sort(rooms, (t1, t2) -> t1[0] == t2[0] ? t1[1]-t2[1] : t1[0]-t2[0]);
        int roomsCnt = 0;
        for(int[] room : rooms) {
            int time = room[0];
            int io = room[1];
            roomsCnt += io;
            answer = Math.max(answer, roomsCnt);
        }
        
        
        return answer;
    }
}