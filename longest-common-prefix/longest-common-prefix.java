class Solution {
    public String longestCommonPrefix(String[] strs) {
       if (strs == null )
           return "";
        
        Arrays.sort(strs);
        StringBuilder str = new StringBuilder();
        char[] first = strs[0].toCharArray();
        char[] last = strs[strs.length -1].toCharArray();
        
        for ( int i=0; i<first.length && i<last.length; i++){
            if (last[i] == first[i] )
                str.append(last[i]);
            else 
                return str.toString();
        }
        return str.toString();
        
    }
}