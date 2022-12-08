class Solution {
    public String defangIPaddr(String address) {
       int len = address.length();
       String res= "";
       for (int i=0; i<len; i++){
           if (address.charAt(i) == '.')
                res+= "[.]";
            else
                res+= address.charAt(i); 
       }
       return res;
    }
}