def smatrix(nums):
    x = []
    y = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] == 0:
                x.append(j)
                y.append(i)
                
    
    for l, m in zip(x, y):            
        for k in range(len(nums[0])):
            nums[m][k] = 0
        for k in range(len(nums)):
            nums[k][l] = 0
              
    return nums            
        
        
nums = [[1,3,4,3],[3,0,2,1],[12,0,4,3]]
print(smatrix(nums))