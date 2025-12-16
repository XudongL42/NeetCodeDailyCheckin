class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                # token is an operator, start compute
                right = int(stack.pop())
                left = int(stack.pop())
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(left / right)
            else:
                # token is just number
                stack.append(token)
        return int(stack.pop())