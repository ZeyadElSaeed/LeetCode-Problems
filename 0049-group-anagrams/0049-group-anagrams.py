class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydiction = dict()
        answer = list()
        for i in range( len(strs) ):
            x = str(sorted( strs[i]))
            if ( x in mydiction):
                mydiction[x].append( strs[i] )      
            else:
                mydiction[x] = [strs[i]]

        for key in mydiction:
            answer.append(mydiction[key])

        return answer        