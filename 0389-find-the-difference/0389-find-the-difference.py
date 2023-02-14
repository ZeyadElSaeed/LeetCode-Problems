class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters_dict = {}
        for x,y in zip( s, t ):
            letters_dict[x] = letters_dict.get(x, 0) + 1
            letters_dict[y] = letters_dict.get(y, 0) - 1
            
        #for the last letter in t as two lengths aren't equal
        letters_dict[ t[-1] ] = letters_dict.get(t[-1], 0) - 1   
        for key in letters_dict:
            if letters_dict[key] < 0:
                return key
            
             
        