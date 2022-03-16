class Solution(object,):
    
    def __init__(self):
        self.dic = {1:1,2:2}
        
    def climbStairs(self, n):
        """
        I wrote first 5 solution on paper and saw a pattern,
        
            f(n)= f(n-1)+f(n-2)
            
        I dont know if this is legal or not but i had to initiate a dictionary.
        Otherwise we had to calculate the result for each step and
        it gives TLE.
        """
        
        if n not in self.dic:
           self.dic[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.dic[n]