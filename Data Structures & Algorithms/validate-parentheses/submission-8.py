class Solution:
    def isValid(self, s: str) -> bool:
        hashmap ={
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        for i in range(len(s)):
            if s[i] in hashmap:
                if stack and hashmap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(s[i])

        return len(stack) == 0