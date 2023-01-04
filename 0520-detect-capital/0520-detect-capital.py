class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        if word.isupper():
            return True
        if word[0].islower():
            return False
        upperNum = 0
        for w in word:
            if (w.isupper()):
                upperNum += 1
                if (upperNum > 1):
                    return False
        return True        
        