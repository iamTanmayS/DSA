def insert(element,sizeofarray,array):
    newarr = [0]  * (sizeofarray+1)
    for i in range(sizeofarray):
        newarr[i] = array[i]
        
    newarr[len(newarr)-1] = element
    return newarr



element = 11

array = [1,2,3,4,5,6,7,8,9,10]

sizeofarray = len(array)
print(insert(element,sizeofarray,array))