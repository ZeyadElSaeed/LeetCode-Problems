class Solution {
    public int[] sortArrayByParity(int[] arr) {
        
        int odd = arr.length - 1;
        int even = 0;
        int i=0;
       while ( even < odd ){
          if ( arr[i] % 2 == 0 ){
              if (even != i){
                 int temp = arr[i] ;
                arr[i] = arr[even];
                arr[even] = temp;
                i--;
              }
              even++;
                
            }
           else{
               if ( odd != i){
               int temp = arr[i] ;
               arr[i] = arr[odd];
               arr[odd] = temp;
               i--; 
               }
               odd--;
           }
           i++;
        }
        return arr;
    }
}