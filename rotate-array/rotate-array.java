class Solution {
    public void rotate(int[] nums, int k) {
        
        k = k % nums.length ;
        int high = nums.length - k ;
        int low = 0;
        
        int[] arr = new int [nums.length];
        int i =0;
        for ( int x : nums )
            arr[i++] = x;
        
        i=0;
        while (high < nums.length)
            nums[i++] = arr[high++];
        
        high = nums.length - k ;
        while ( low < high ){
            System.out.println(low);
            nums[i++] = arr[low++];
            
        }
            
            
        
        
    }
}