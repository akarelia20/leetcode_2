class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            
                if tokens[i] == '+':
                    stack.append(stack.pop()+stack.pop())
                elif tokens[i] == '-':
                    op= (stack[-2] - stack.pop())
                    stack.pop()
                    stack.append(int(op))
                elif tokens[i] == '*':
                    stack.append(stack.pop()*stack.pop())
                elif tokens[i] == '/':
                    op= (stack[-2]/stack.pop())
                    stack.pop()
                    stack.append(int(op))
                else:
                    stack.append(int(tokens[i]))
                
        
        return stack[-1] 