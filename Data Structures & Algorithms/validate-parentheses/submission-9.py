class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n & 1:  # odd length can never be balanced
            return False

        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for i, ch in enumerate(s):
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
                if len(stack) > n - i - 1:  # not enough characters left to close them all
                    return False

        return not stack