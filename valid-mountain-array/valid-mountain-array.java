class Solution {
    public boolean validMountainArray(int[] arr) {
        int count = 0;
        boolean up = true;
        if (arr.length >= 3){
            boolean flag = false;
            for (int i=0; i<arr.length-1; i++){
                if ( arr[i] == arr[i+1] )
                    return false;
                else if (arr[i] < arr[i+1] && !up)
                    return false;
                else if (arr[i] > arr[i+1] ){
                    up = false;
                    count++;
                }
            }
            if (!up && count != arr.length-1)
            return true;
        }
            return false;
        
    }
}