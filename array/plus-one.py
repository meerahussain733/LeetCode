class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits=digits
        new_digits[-1]+=1
        return new_digits
        