class Solution {
    public int[] twoSum(int[] num, int target) {
        int first = 0;
        int last = num.length-1;
        int[] res = new int [2];
        while ( first < last ){
            if ( num[first] + num[last] == target ){
                res[0] = first +1;
                res[1] = last + 1;
                break;
            }
            else if ( num[first] + num[last] > target  )
                last--;
            else if ( num[first] + num[last] < target )
                first++;       
        }
            return res;
    }
}