class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i=="+":
                a=s.pop()
                b=s.pop()
                c=a+b
                s.append(int(c))
            elif i=="*":
                a=s.pop()
                b=s.pop()
                c = a*b
                s.append(int(c))
            elif i=="/":
                a=s.pop()
                b=s.pop()
                c = b/a
                s.append(int(c))
            elif i=="-":
                a=s.pop()
                b=s.pop()
                c = b - a
                s.append(int(c))
            else:
                s.append(int(i))
        return s[0]
        
        

                
        