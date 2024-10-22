def signsbrutforce(nums):
        nli =[]
        pli= []
        num = []
        for i in range(len(nums)):
            if nums[i]<0:
                nli.append(nums[i])
            else:
                pli.append(nums[i])
                
        for j in range(len(nums)//2):
           num.append(pli[j])
           num.append(nli[j])
        return num
            
           
        
    
  
