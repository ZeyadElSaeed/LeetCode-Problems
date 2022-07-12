class Solution {
    public void duplicateZeros(int[] arr) {
        for(int i=0; i<arr.length; i++){
            if (arr[i]==0){
                shift(arr, i+1);
                i+=1; 
                if (i != arr.length ){
                arr[i] = 0;
                }
            }
        }
        
    }
    public void shift(int [] arr , int index){
        for ( int i=arr.length-1; i>index; i--){
            arr[i] = arr[i-1];
        }
    }
}