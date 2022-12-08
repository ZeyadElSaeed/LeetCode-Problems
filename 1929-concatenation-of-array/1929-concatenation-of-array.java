class Solution {
    public int[] getConcatenation(int[] nums) {
        int size = nums.length;
        int[] ans = new int [size*2];
        for ( int i=0; i<2; i++)
            for ( int j=0; j<size; j++)
                if ( i == 0)
                    ans[j] = nums[j];
                else
                    ans[j + size] = nums[j]; 

        return ans;                
    }
}