class Solution {
    public int[][] updateMatrix(int[][] mat) { 
        int n = mat[0].length , m = mat.length , i=0 , j=0;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new LinkedList<int[]>();
        
        for(i=0; i<m; i++)
            for(j=0; j<n; j++){
                if ( mat[i][j] == 0){
                    q.offer(new int[] {i , j});
                    visited[i][j] = true;
                }
            } 
        
        while ( !q.isEmpty() ){
            int[] curr = q.poll();
            for ( int[] d: dirs){
                int x = curr[0] + d[0];
                int y = curr[1] + d[1];
                
                if ( outOfBounds(mat , x ,y) || visited[x][y] )continue;
                visited[x][y] = true;
                mat[x][y] = mat[curr[0]][curr[1]] + 1;
                q.offer( new int[] {x ,y});
            }
        }
        return mat;
    }
    
    
    
    
    boolean outOfBounds( int[][] mat , int i , int j){
        return i < 0 || i >= mat.length || j < 0 || j >= mat[0].length;
    }
    
}