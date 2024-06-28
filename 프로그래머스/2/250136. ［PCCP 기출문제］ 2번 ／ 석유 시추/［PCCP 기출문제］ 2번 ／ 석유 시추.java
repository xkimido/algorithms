import java.util.*;

class Solution {

    boolean[][] visited;

    Map<Integer, Integer> groupSize = new HashMap<>();

    Group[][] groups;

    int index = 0;

    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};

    int n;
    int m;
    int[][] land;

    public int solution(int[][] land) {
        int answer = 0;

        this.n = land.length;
        this.m = land[0].length;
        this.land = land;

        groups = new Group[n][m];
        visited = new boolean[n][m];

        LinkedList<Integer[]> queue = new LinkedList<>();

        for(int i = 0; i<land.length; i++){
            for(int j = 0 ; j<land[0].length; j++){
                if(land[i][j] != 0 && !visited[i][j]){
                    visited[i][j] = true;
                    queue.add(new Integer[]{i,j});
                    Group group = new Group(index);
                    index++;
                    groups[i][j] = group;
                    setGroup(queue, group);
                }
            }
        }

        for(int i = 0; i<m; i++){
            answer = Math.max(getGroup(i), answer);
        }

        return answer;
    }

    void setGroup(LinkedList<Integer[]> queue, Group group){        
        int size = 1;

        while(!queue.isEmpty()){
            Integer[] cur = queue.poll();
            for(int i = 0 ; i<4; i++){
                int nextR = cur[0] + dy[i];
                int nextC = cur[1] + dx[i];
                if(
                    isPossible(nextR, nextC) &&
                    !visited[nextR][nextC] &&
                    land[cur[0]][cur[1]] == land[nextR][nextC]
                  ){
                    visited[nextR][nextC] = true;
                    groups[nextR][nextC] = group;
                    size++;
                    queue.add(new Integer[]{nextR, nextC});
                }
            }
        }

        groupSize.put(group.index, size);
    }

    boolean isPossible(int r, int c){
        if(r<0 || c<0 || r>=n || c>=m){
            return false;
        }
        return true;
    }

    int getGroup(int col){
        int sum = 0;

        Set<Integer> set = new HashSet<>();

        for(int i = 0; i<n; i++){
            if(land[i][col]!=0){
                set.add(groups[i][col].index);
            }
        }

        for(Integer index : set){
            sum += groupSize.get(index);
        }

        return sum;
    }
}

class Group{
    int index;

    Group(int index){
        this.index = index;
    }
}