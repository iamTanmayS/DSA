def countSubstr (s, k):
    
        i = 0
        j = 0
        n = len(s)
        count = 0
        subs = ""
        if len(s) <=k:
            return 0
        while(j <= n):
            while(i<n):
                if len(subs) < k:
                    subs+= s[i]
                    i+=1
                elif len(subs) == k:
                    count+=1
                i+=1
            i = 0
            j+=1
            k+=1
            
        return count
s = "aba"
k = 2
print(countSubstr(s,k))
