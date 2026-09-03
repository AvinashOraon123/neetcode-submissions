class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []
        if len(s)==1:
            return False
        elif len(s)==0:
            return True
        else:
            for i in range(len(s)):
                if s[i]== '(' or s[i]== '[' or s[i]== '{':
                    stack.append(s[i]) 
                if s[i] == ')' or s[i]== ']' or s[i]== '}':
                    if len(stack) == 0:
                        return False
                    elif hashmap[stack.pop()] != s[i]:
                        return False

        return True


        