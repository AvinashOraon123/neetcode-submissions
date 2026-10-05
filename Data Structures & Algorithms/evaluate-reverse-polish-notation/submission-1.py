class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            try:
                stack.append(int(tokens[i]))
            except ValueError:
                b = stack.pop()   # right operand (top of stack)
                a = stack.pop()   # left operand

                if tokens[i] == '+':
                    res = a + b
                elif tokens[i] == '-':
                    res = a - b
                elif tokens[i] == '*':
                    res = a * b
                else:
                    res = int(a / b)   # truncate toward zero

                stack.append(res)

        return stack[-1]