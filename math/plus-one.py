class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = int("".join(map(str, digits))) +1
        new_digits = [int(digit) for digit in str(new_digits)]
        return new_digits
        