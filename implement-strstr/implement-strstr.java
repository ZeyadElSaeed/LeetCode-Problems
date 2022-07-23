class Solution {
    public int strStr(String haystack, String needle) {
        int len1 = haystack.length();
        int len2 = needle.length();
        
        if (haystack==null || needle==null)
            return 0;
        
        for (int i=0; i<len1; i++){
            int count = 0;
            while ( count < len2 && count+i < len1 && haystack.charAt(count+i) == needle.charAt(count))
                count++;
            if (count == len2 )
                return i;
        }
        
        return -1;
        
        
    }
}