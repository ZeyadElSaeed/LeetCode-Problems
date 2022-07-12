class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int max = 0 ;
        for (int x : nums ){
            if (x == 1){
                count ++ ;
            }
            else{
                if ( max < count )
                    max = count;
                count = 0;
            }
        }
        if ( max < count )
            max = count;
        return max ;
        
    }
}