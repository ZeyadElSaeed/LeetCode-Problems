import java.util.*;
import java.awt.Point;
class Solution {
    public int numSquares(int n) {
        int[] visited = new int[n+1];
        Queue<Point> q = new LinkedList<>();
        int ans = Integer.MAX_VALUE;
        
        visited[n] = 1;
        q.add( new Point( n , 0) );
        
        while( q.size() != 0){
            Point p = q.peek();
            q.remove();
            
            if ( p.x == 0) ans = Math.min( ans , p.y );
            
            for ( int i=1; i*i<=n; i++){
                if ( p.x - i*i >= 0  && (visited[p.x - i*i] == 0) ){
                    visited[p.x - i*i] = 1;
                    q.add( new Point(p.x - i*i , 1+p.y));
                }
            }
        }
        return ans;
    }
}