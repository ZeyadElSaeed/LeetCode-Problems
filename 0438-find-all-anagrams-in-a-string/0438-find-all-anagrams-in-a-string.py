class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        # intialize two dictonarys to comapre them with each other
        s_dict, p_dict = {}, {}
        len_s = len(s)
        len_p = len(p)
        
        #check if the first len(p) letters are Anagram
        for i in range( len_p ):
            s_dict[ s[i] ] = s_dict.get(s[i] , 0 ) + 1
            p_dict[ p[i] ] = p_dict.get(p[i] , 0 ) + 1

        answer = [0] if s_dict == p_dict else []
        left = 0
        # each iteration we add one more letter form the right 
        # and remove the leftmost letter in the dictionary form s
        for i in range(len_p, len_s ):
            s_dict[ s[i] ] = s_dict.get(s[i] , 0 ) + 1
            s_dict[ s[left] ] -= 1
            
            if s_dict[ s[left] ] == 0:
                s_dict.pop( s[left] )
            left += 1
            
            if s_dict == p_dict:
                answer.append(left)
                
        return answer
        