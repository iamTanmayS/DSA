def rotatembrute(nums):
    
    y=[]
    for i in range(len(nums)):
        x=[]
        for j in range(len(nums)-1,-1,-1):
            x.append(nums[j][i])
        y.append(x)
        
    return y

print(rotatembrute([[1,2,3],[4,5,6],[7,8,9]]))
                
               
def rotatemoptimal(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j], matrix[j][i]= matrix[j][i],matrix[i][j]
    for k in range(len(matrix)):
        matrix[k].reverse()
    return matrix