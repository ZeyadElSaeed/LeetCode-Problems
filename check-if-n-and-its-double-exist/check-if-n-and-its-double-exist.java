class Solution {
    public boolean checkIfExist(int[] arr) {
        for ( int i=0; i<arr.length; i++){
            int x = arr[i];
            for (int j=i+1; j<arr.length;j++){
                if ( x*2 == arr[j] || arr[j]*2 == x)
                    return true;
            }
        }
        return false;
    }
}