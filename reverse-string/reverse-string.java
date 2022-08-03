class Solution {
    public void reverseString(char[] s) {
        rev( s , 0, s.length-1);
    }
    void rev( char[] s , int f, int l ){
        if ( f >= l) return;
            char temp = s[f];
            s[f] = s[l];
            s[l] = temp;
            rev ( s , ++f, --l);
    }
}