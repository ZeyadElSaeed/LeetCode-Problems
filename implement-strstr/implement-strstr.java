class Solution {
    public int strStr(String haystack, String needle) {
        int len1 = haystack.length();
        int len2 = needle.length();
        
        if (len2==0)
            return 0;
        
        return haystack.indexOf(needle);
    }
}