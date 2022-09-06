class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                stack.append(-stack.pop() + stack.pop())
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                stack.append(int((1/stack.pop())*stack.pop()))
            else:
                stack.append(int(char))
        return stack[0]