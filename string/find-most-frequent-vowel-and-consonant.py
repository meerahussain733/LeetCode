class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_map={'a':0,'e':0,'i':0,'o':0,'u':0}
        const_map={}
        for char in s:
            if char in vowel_map:
                vowel_map[char]+=1
            else:
                if char in const_map:
                    const_map[char]+=1
                else:
                    const_map[char]=1
        max_const=0
        max_const=max(const_map.values(),default=0)
        return max(vowel_map.values())+max_const
        