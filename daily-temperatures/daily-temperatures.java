class Solution {
    public int[] dailyTemperatures(int[] temp) {
        int[] ans = new int [temp.length];
        Stack<Integer> st = new Stack<Integer>();
        for( int i=0; i<temp.length; i++){
            if ( st.size() == 0 ){
                st.add(i);
                continue;
            }
            else {
                while ( st.size() != 0 && temp[st.peek()] < temp[i]  ){
                    ans[st.peek()] = i-st.peek();
                    st.pop();
                }
                st.push( i);
            }
        }
        return ans;
    }
}