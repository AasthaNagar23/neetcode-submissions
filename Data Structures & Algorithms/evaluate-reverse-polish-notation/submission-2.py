class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b=stack.pop()  # b pehle aaega then a 
                a=stack.pop()
                if token=="+":
                    stack.append(a+b)
                elif token=="-":
                    stack.append(a-b)
                elif token=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[-1]