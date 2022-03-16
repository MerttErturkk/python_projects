class Solution:
    def __init__(self):
        self.dic ={0:0,1:1}
        
    def fib(self, n: int):
        if n in self.dic:
            return self.dic[n]
        else:
            self.dic[n] = self.fib(n-2)+ self.fib(n-1)
        return self.dic[n]
        
        
        
        
        