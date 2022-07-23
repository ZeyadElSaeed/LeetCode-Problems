class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        String[] str = s.trim().split("\\s+");
        System.out.println( Arrays.toString( str));
        int len = str.length;
        for ( int i=len-1; i>=0; i--){
            if ( i == 0 ){
                 res.append(str[i]);
            }
            else {
                res.append(str[i]);
                res.append(" ");
            }    
        }
        return res.toString() ;
        
    }
}