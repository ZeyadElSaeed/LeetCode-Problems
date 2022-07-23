class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int low = 0;
        int high = 0;
        int sum = 0;
        int min = Integer.MAX_VALUE;
        int l = nums.length;
        
        if ( nums == null || nums.length == 0 )
            return 0;
        
        while ( high < l ){
            sum+=nums[high];
            if ( sum >= target){
                while ( sum - nums[low] >= target && low < high ){
                    sum -= nums[low++];
                }
                min = Math.min( min , high - low + 1 );
            }
            high+=1;
        }
        return (min != Integer.MAX_VALUE ? min : 0);
  
    }
}