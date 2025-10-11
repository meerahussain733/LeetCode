class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        char_hash={}
        left=0
        for right in range(len(s)):
            character=s[right]
            if character in char_hash and char_hash[s[right]]>=left:
                left=char_hash[character]+1
            char_hash[character]=right
            current_len= right - left+1
            max_len=max(max_len,current_len)
        return max_len


        