class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int zero_ptr = 0;
        int temp_val = 0;
        for ( int i=0; i<n; i++){
            if (nums[i] != 0){
                temp_val = nums[i];
                nums[i] = nums[zero_ptr];
                nums[zero_ptr] = temp_val;
                zero_ptr++;
            }
        }
            
    }
}