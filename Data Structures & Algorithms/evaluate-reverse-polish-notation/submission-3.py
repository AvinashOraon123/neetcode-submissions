class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res= 0
        for i in tokens:
            try:
                stack.append(int(i))
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    res = a + b
                elif i == '-':
                    res = a - b
                elif i == '*':
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(res)
        return res