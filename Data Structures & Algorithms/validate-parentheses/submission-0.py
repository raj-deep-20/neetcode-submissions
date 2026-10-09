class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        fmap = {")":"(", "]":"[","}":"{"}

        for c in s:
            if c in fmap:
                if stack and stack[-1] == fmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False