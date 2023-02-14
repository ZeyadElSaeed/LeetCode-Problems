class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # dictionary to give each letter an ordered index
        letter_to_index = {}
        for i in range(len(order)):
            letter_to_index[order[i]] = i

        #check the order of two words 
        def isOrdered(w1: str, w2: str) -> bool:
            for x, y in zip( w1, w2):
                if letter_to_index[x] == letter_to_index[y]:
                    continue
                return letter_to_index[x] < letter_to_index[y]
            return True if len(w1) <= len(w2) else False

        for i in range(1, len(words)):
            if not isOrdered(words[i-1] , words[i]):
                return False
        return True        