class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result=0
        for i in range(len(s)):
            count, max_freq={},0
            for j in range(i,len(s)):
                count[s[j]]=1+count.get(s[j],0)
                max_freq = max(max_freq, count[s[j]])
                if (j - i + 1) - max_freq <= k:
                    result= max(result, j - i + 1)
        return result
        