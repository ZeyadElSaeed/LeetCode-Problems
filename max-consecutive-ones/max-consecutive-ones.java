class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int max = 0 ;
        for (int x : nums ){
            if (x == 1){
                count ++ ;
            }
            else{
                max = Math.max( max , count );
                count = 0;
            }
        }
        max = Math.max( max , count );
        return max ;
        
    }
}