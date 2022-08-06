class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<Character>();
        for ( int i=0; i<s.length();i++ ){
            if ( s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                st.push( s.charAt(i) );
            else { 
                if ( (st.size() == 0) || (s.charAt(i) == ')' && st.peek() != '(') || (s.charAt(i) == '}' && st.peek() != '{') || (s.charAt(i) == ']' && st.peek() != '[') )
                    return false;
                else 
                    st.pop();
            }
        }
        
        if ( st.size() > 0) return false;
        return true;
    }
}