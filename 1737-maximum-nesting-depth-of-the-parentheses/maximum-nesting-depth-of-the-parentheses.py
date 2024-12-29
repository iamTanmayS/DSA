class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        temp = 0
        for i in s:
            if i == "(":
                count+=1
            
            
            
            elif i ==")":
                count-=1
            
            temp = max(count,temp)


        return temp
        