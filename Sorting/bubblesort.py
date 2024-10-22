def bubble(x):
    
    for i in range(len(x)):
        flag = 0 
        for j in range(len(x) - 1 - i):
            if x[j]>x[1+j]:
                x[j], x[j+1]  = x[j+1] ,x[j]
                flag= 1
        if flag==0:
            break
    return(x)


print(bubble([1,21,32,1,2,1,2,1,23,4,5,7,5,4,3,276]))