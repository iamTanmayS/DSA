def maxSubArray(nums):
        li = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                a = nums[i:j]
                li.append(a)

        dic = {}
        for i in li:
            j = 0
            sum = 0
            while(len(i)>j):
                sum = sum+i[j]
                j+=1
            dic[tuple(i)] = sum
        
        g = max(dic.values())
        for i in dic:
            if dic[i] == g:
                return list(i)
             
        
print(maxSubArray([1,3,4,2,1,3,2,3]))