class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        
        int i=0;
        int j=0;
        
        Queue<Character> q = new LinkedList<Character>();
        for(i=0; i<m; i++)
            for (j=0; j<n; j++)
                if( grid[i][j] == '1')
                    count += solve(q , grid ,i ,j , n ,m );
        return count;
    }
    
     public int solve( Queue<Character> q ,char[][] grid ,int i ,int j ,int n ,int m){
        q.add(grid[i][j]);
        grid[i][j] = '0';
        while ( q.size() != 0 && q.peek() == '1'){
            char x = q.peek();
            q.remove();
            
            if ( i-1 >= 0 && grid[i-1][j] == '1'){
                solve ( q , grid , i-1 , j , n , m);
            }
            if ( i+1 < m && grid[i+1][j] == '1'){
                solve ( q , grid , i+1 , j , n , m);
            }
            if ( j-1 >= 0 && grid[i][j-1] == '1'){
                solve ( q , grid , i , j-1 , n , m);
            }
            if ( j+1 < n && grid[i][j+1] == '1'){
                solve ( q , grid , i , j+1 , n , m);
            }
        }
        return 1;
    }
}