class Solution {
    public void moveZeroes(int[] arr) {
        int count = 0;
        for (int i=0; i<arr.length; i++){
            if (arr[i] == 0 ){
                for (int j=i; j<arr.length-1; j++)
                    arr[j] = arr[j+1];
                arr[ arr.length-1 ] = 1;
                i--;
                count++;
            }
        }
        for (int i = 0; i<count; i++){
            arr[ arr.length-1-i] = 0;
        }
    }
}