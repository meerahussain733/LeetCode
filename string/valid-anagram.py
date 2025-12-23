class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_map={}
        for char in s:
            if char in freq_map:
                freq_map[char]+=1
            else:
                freq_map[char]=1
        for char in t:
            if char not in freq_map:
                return False
            freq_map[char]-=1
            if freq_map[char]< 0:
                return False
        return True

        
        
        