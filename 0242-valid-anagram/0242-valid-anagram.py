class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        s = list(s)
        if ( len(t) != len(s)):
            return False
        
        for letter in s:
            if ( letter in t):
                t.remove(letter)
            else:
                return False    
        return True         