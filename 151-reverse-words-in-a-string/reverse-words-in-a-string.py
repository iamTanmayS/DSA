class Solution:
    def reverseWords(self, s: str) -> str:
        arr = ""
        words = []
        n = len(s)
        i = 0
        while(i<n):
            
            if s[i] == " ":
                i+=1
                if len(arr)>0:
                    words.append(arr)
                    arr = ""
            elif s[i]!=" ":
                arr+=s[i]
                i+=1
        if len(arr)>0:
            words.append(arr)
            
        return " ".join(words[::-1])

        
                    
        
            
            
