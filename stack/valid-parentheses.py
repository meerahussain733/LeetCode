class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        pair={')':'(',']':'[','}':'{' }
        stack=[]
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack[-1]!=pair[ch]:
                    return False
                stack.pop()
        if len(stack)==0:
            return True
        return False