class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False

        match = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for ch in s:
            if ch in match:
                stack.append(match[ch])  # push the expected closer
            elif not stack or stack.pop() != ch:
                return False

        return not stack