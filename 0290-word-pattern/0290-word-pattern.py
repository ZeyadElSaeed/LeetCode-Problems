class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        patternList = list(pattern)
        n = len(sList)
        my_dictionary = dict()
        check = dict()
        if len(sList) != len(patternList):
            return False

        for i in range(n):
            if patternList[i] in my_dictionary:
                if (my_dictionary[patternList[i]] != sList[i]):
                    return False
            else :
                my_dictionary[patternList[i]] = sList[i]

        for val in my_dictionary:
            if my_dictionary[val] in check:
                return False
            else:
                check[my_dictionary[val]] = [val]
        return True        
        