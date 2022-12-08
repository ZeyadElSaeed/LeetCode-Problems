class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int size = operations.length;
        int ans = 0;
        for ( int i=0; i<size; i++){
            if ( operations[i].equals("++X") || operations[i].equals("X++") )
                ans++;
            if (operations[i].equals("--X")  || operations[i].equals("X--") )
                ans--;
        }
        return ans;
    }
}