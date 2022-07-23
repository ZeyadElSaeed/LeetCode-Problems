class Solution {
    public String reverseWords(String s) {
        StringBuilder str = new StringBuilder();
        String[] arr = s.split(" ");
        System.out.println( Arrays.toString(arr) );
        
        for ( int i=0; i<arr.length; i++){
            for ( int j=arr[i].length()-1; j>=0; j--){
                str.append( arr[i].charAt(j));
            }
            if ( i != arr.length-1 )
                str.append(" ");
        }
        
        return str.toString();
    }
}