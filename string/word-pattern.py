class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        nw_str=s.split(' ')
        hash_map={}
        if len(pattern)!=len(nw_str):
            return False
        if len(set(pattern))!= len(set(nw_str)):
            return False
        for i in range(len(nw_str)):
            if nw_str[i] not in hash_map:
                hash_map[nw_str[i]]=pattern[i]
            elif hash_map[nw_str[i]]!=pattern[i]:
                return False
        return True
            

        