class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        for ( int i=0; i< nums.length; i++ ){
            if ( nums[i] == val ){
                sort(nums , i);
                i--;
                count++;
            }
            else if (nums[i] == -1)
                continue;
        }
        System.out.println(Arrays.toString(nums));
        return nums.length-count;
        
        
    }
    
    public void sort(int [] num , int index){
        for (int i=index; i<num.length-1; i++){
            num[i] = num[i+1];
        }
        num[num.length-1] = -1;
    }
}