class Solution {
    public int dominantIndex(int[] nums) {
        int max = nums[0];
        int index = 0;
        for (int i=0; i<nums.length; i++)
            if (max < nums[i] ){
                 max = nums[i];
                 index = i;
            }
        System.out.println(max + " : " + index);
        boolean flag = true;
        for (int i=0; i<nums.length; i++){
            if (i == index )
                continue;
            else if (max < 2*nums[i] )
                flag = false;
        }
        if (flag)
            return index;
        return -1;
        
    }
}