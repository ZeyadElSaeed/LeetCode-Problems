class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for ( int x : nums ){
            if ( (x>9 && x<100) || (x>999 && x<10000) || (x>99999)&& x<1000000 )
                count++;
        }
        return count;
        
    }
}