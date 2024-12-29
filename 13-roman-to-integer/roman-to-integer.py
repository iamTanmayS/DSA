class Solution:
    def romanToInt(self, s: str) -> int:
        romandic = {"I" : 1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        for i in range(len(s)):
            sum+=romandic[s[i]]
            if i> 0 and (s[i] == "V" or s[i] == "X")  and s[i-1]  =="I":
                sum-=2
            if i> 0 and (s[i] == "L" or s[i] == "C") and s[i-1]  =="X":
                sum-=20
            if i> 0 and (s[i] == "D" or s[i] == "M")  and s[i-1]  =="C":
                sum-=200
        return sum
            
        

        