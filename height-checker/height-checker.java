class Solution {
    public int heightChecker(int[] heights) {
        int len = heights.length;
        int [] temp = new int [len];
        for (int i=0; i<len; i++)
            temp[i] = heights[i];
        Arrays.sort(temp);
        int count=0;
        for ( int i =0; i<len; i++){
            if (heights[i] != temp[i] )
                count++;
        }
        return count;
    }
}