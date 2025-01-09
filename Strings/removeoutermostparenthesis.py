def reverseWords(s):
        arr = ""
        n = len(s)
        strarr = []
        i = 0

        while(i<n):
            char = s[i]
            if char!= " ":
                arr+=char
                i+=1
            elif char == " ":
                    i+=1
                    if len(arr)>0:
                            strarr.append(arr)
                            arr = ""
        if len(arr)>0:
                strarr.append(arr)               
        arr = ""  
        
        i = len(strarr)-1
        while(i>=0):
                if i== 0:
                        arr += strarr[i] 
                        i-=1
                else:
                        arr += strarr[i] + " "
                        i-=1
                
        
            
            
                
            
        return arr
            
            

           
