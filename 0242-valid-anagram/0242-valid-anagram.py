class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ( len(t) != len(s)):
            return False
        dictionary = {}
        for char in s:
            dictionary[char] = dictionary.get(char, 0 ) + 1
            
        for char in t:
            if char not in dictionary:
                return False
            elif dictionary[char] <= 0:
                return False
            else:
                dictionary[char] -= 1
        return True         