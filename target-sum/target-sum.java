class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int count = 0;
        count += solve( nums , 0 , target , 0);
        return count;
        
        
    }
    int solve ( int[] nums , int i , int target , int total){
        if ( i >= nums.length){
            if ( total == target ) return 1;
            else return 0;
        }
        return solve ( nums , i + 1 , target , total + nums[i]) + solve ( nums , i + 1 , target , total - nums[i]);
        
    }
}