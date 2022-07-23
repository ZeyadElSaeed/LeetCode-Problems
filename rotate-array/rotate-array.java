class Solution {
    public void rotate(int[] nums, int k) {
        
        k = k % nums.length ;
        int len = nums.length;
        
        reverse( nums , 0 , len- 1 );
        reverse( nums , 0 , k-1);
        reverse( nums , k , len-1);
        
        
    }
    public void reverse( int[] arr , int left , int right){
        while ( left < right ){
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++; right--;
        }
    }
}