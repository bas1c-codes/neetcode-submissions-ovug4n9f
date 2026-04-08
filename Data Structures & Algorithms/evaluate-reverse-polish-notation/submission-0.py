class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
      #if len(tokens)==1:
      #      return int(tokens[0])
        ops={
            "+":lambda a,b:a+b,
            "-":lambda a,b:a-b,
            "*":lambda a,b:a*b,
            "/":lambda a,b:int(a/b)
        }
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(ops[i](a,b))
        return stack[-1]