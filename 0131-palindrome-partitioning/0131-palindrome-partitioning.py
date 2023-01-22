class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(s , path:List[str], res: List[str]):
            if not s:
                return res.append(path[:]) 
            for i in range( 1, len(s) + 1):
                if ( s[:i] == s[i-1:: -1]):
                    path.append(s[:i])
                    backtrack( s[i:],  path, res  )
                    path.pop()
        res = []
        backtrack(s,[], res)
        return res        