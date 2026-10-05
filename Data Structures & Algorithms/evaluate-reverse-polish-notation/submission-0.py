class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0

        stack = []

        for i in range(len(tokens)):
            try:
                stack.append(int(tokens[i]))
            except ValueError:
                if tokens[i] == '+':
                    res= stack[0] + stack[1]
                    stack.clear()
                    stack.append(res)
                elif tokens[i] == '-':
                    res= stack[0] - stack[1]
                    stack.clear()
                    stack.append(res)
                elif tokens[i] == '*':
                    res= stack[0] * stack[1]
                    stack.clear()
                    stack.append(res)
                else :
                    res= stack[0] / stack[1]
                    stack.clear()
                    stack.append(res)
        return res

            