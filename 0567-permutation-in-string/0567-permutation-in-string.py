class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getDict(s):
            dictionary = {}
            for letter in s:
                dictionary[letter] = dictionary.get(letter, 0) + 1
            return dictionary
            
        #take letters == len(s1) and make them a dict
        left = 0
        right = len(s1)
        ref_dict_s1 = getDict(s1)
        while right < len(s2) + 1:
            if ref_dict_s1 == getDict(s2[left:right]):
                return True
            else:
                left += 1
                right += 1
                
        return False
            
        