class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<Integer>();
        int first = 0;
        int second = 0;
        int res = 0;
        for ( int i=0; i< tokens.length; i++)
            if ( tokens[i].equals("+") || tokens[i].equals("*") || tokens[i].equals("-") ||                                      tokens[i].equals("/")){
                second = st.pop();
                first = st.pop();   
                switch( tokens[i]){
                case "+":res = first + second;break;
                case "-":res = first - second;break;
                case "*":res = first * second;break;
                default:res = first / second;break;   
            }
                st.add( res );
            }
                else {
                    st.add( Integer.parseInt( tokens[i]) );
                }
        return st.pop();
    }
}