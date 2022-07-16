class Solution {
    public int thirdMax(int[] arr  ) {
        Arrays.sort(arr);
        int len = arr.length;
        int max = arr[ len-1 ];
        int count = 1;
        
        for ( int i=len-2; i>=0 && count < 3; i-- ){
            if ( max > arr[i] ){
                max = arr[i];
                count++;
            }      
        }
        
        if (count == 3 )
            return max ;
        else 
            return arr[len-1];
    }
}