class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            try:
                stack.append(int(i))
            except ValueError:
                if i == '+':
                    stack.append(stack.pop()+ stack.pop())
                elif i == '-':
                    stack.append(stack.pop()- stack.pop())
                elif i == '*':
                    stack.append(stack.pop()* stack.pop())
                else:
                    stack.append(int(stack.pop()/ stack.pop()))
 
        return stack[-1]