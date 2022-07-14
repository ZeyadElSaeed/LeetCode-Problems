class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 0;
        for ( int i=0; i<nums.length; i++){
            int x = nums[i];
            for ( int j = i+1; j<nums.length; j++){
                if ( x == 101 || x != nums[j] )
                    break;
                else {
                    nums[j] = 101;
                    count++;
                }
            }
        }
        Arrays.sort(nums);
        return nums.length - count;
        
    }
    
}