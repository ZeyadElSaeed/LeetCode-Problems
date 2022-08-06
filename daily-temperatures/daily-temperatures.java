import java.awt.Point;
class Solution {
    public int[] dailyTemperatures(int[] temp) {
        int[] ans = new int [temp.length];
        Arrays.fill(ans, 0);
        Stack<Point> st = new Stack<Point>();
        for( int i=0; i<temp.length; i++){
            if ( st.size() == 0 ){
                st.add( new Point(temp[i] , i));
                continue;
            }
            else {
                while ( st.size() != 0 && st.peek().x < temp[i]  ){
                    ans[st.peek().y] = i-st.peek().y;
                    st.pop();
                }
                st.push( new Point( temp[i] , i));
            }
        }
        return ans;
    }
}