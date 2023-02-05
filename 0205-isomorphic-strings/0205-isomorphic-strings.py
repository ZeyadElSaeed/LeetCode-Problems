class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_dict_s = {}
        mapping_dict_t = {}

        for x , y in zip( s, t):
            # check if every letter in s maps to one letter in t
            if x in mapping_dict_s:
                if mapping_dict_s[x] != y:
                    return False
            else:
                mapping_dict_s[x] = y
            # check if every letter in t maps to one letter in s
            if y in mapping_dict_t:
                if mapping_dict_t[y] != x:
                    return False
            else:
                mapping_dict_t[y] = x
        return True        