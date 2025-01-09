def reverseWords(s):
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
            else:
                arr+=s[i]
                i+=1
        if len(arr)>0:
            words.append(arr)
        print(words)
        return " ".join(words[::-1])

        
                    
        
            
            
print(reverseWords("a good example"))