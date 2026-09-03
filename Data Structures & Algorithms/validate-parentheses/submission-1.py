class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack1 = []
        stack2 = []

        for i in enumerate(s):
            if i == '(' or i == '[' or i == '{' :
                stack1.append(i)

        for i in enumerate(s):
            if i == ')' or i == ']' or i == '}' :
                stack2.append(i)

        for i in range(len(stack1)):
            if stack2[i]!=hashmap[stack1[i]]:
                return False
        return True


        