class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int m = image.length;
        int n = image[0].length;
        boolean[][] visited = new boolean[m][n];
        solve ( color ,visited, image , sr , sc , n , m);
        return image;
        
    }
    public void solve( int x , boolean[][] visited ,int[][] grid ,int i ,int j ,int n ,int m){
        visited[i][j] = true;
        int y = grid[i][j];
        grid[i][j] = x;
            if ( i-1 >= 0 && !visited[i-1][j] && grid[i-1][j] == y){
                solve ( x ,visited, grid , i-1 , j , n , m);
            }
            if ( i+1 < m && !visited[i+1][j] && grid[i+1][j] == y){
                solve ( x ,visited, grid , i+1 , j , n , m);
            }
            if ( j-1 >= 0 && !visited[i][j-1] && grid[i][j-1] == y){
                solve ( x ,visited, grid , i , j-1 , n , m);
            }
            if ( j+1 < n && !visited[i][j+1] && grid[i][j+1] == y){
                solve ( x ,visited, grid , i , j+1 , n , m);
            }
        
    }
}