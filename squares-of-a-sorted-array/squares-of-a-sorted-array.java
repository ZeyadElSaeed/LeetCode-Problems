import java.util.Arrays;   
class Solution {
    public int[] sortedSquares(int[] nums) {
        for(int i=0; i<nums.length; i++ ){
            int squ = nums[i]*nums[i];
            nums[i]=squ;
        }
        Arrays.sort(nums);
        return nums;
        
    }
}