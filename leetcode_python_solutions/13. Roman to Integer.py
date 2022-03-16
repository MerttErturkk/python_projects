class Solution:
    def romanToInt(self, s: str) -> int:

        coefs = {
                 "I":1 , "V":5 , "X":10 ,
                 "L":50 , "C":100 , "D":500,
                 "M":1000
                 }
        
        relat = {
                 "I":set(["V","X"]),
                 "X":set(["L","C"]),
                 "C":set(["D","M"])
                }
        
        check= set(["I","X","C"])
        
        decimal = 0
        
        for i in range(len(s)):
            if s[i] in check:
                try:
                    if s[i+1] in relat[s[i]]:    
                        decimal -= coefs[s[i]]
                    else:
                        decimal +=coefs[s[i]]
                except:
                    decimal +=coefs[s[i]]
            else:
                decimal +=coefs[s[i]]
        
        return decimal