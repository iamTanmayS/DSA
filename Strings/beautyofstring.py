def substrings(s):
        n = len(s)
        substring = []
        dic = {}
        temp = 0
        sum = 0
        for i in range(n):
            for j in range(i+1,n):
                substring.append(s[i:j+1])
    
        for i in substring:
            dic.clear()
            for j in i:
                if j not in dic:
                    dic[j] = 1
                else:
                    dic[j] += 1
            
            frequencies = [freq for freq in dic.values() if freq > 0]
            temp = max(frequencies) - min(frequencies) 
            sum += temp
            temp = 0
            
        return sum
            
            
        
    
            
            
print(substrings('aabcebba'))