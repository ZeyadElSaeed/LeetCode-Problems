class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int right = numbers.length -1;
        int left = 0;
        int sum = 0;
        int [] res = new int [2];
        while (left < right){
            sum = numbers[right] + numbers[left];
            if (sum == target){
                res[0] = left + 1;
                res[1] = right + 1;
                return res;
            }
            if (sum<target){
                left++;
            }
            else{
                right--;
            }
        }
        res[0] = -1;
        res[1] = -1;
        return res;
        
    }
}