#User function Template for python3


    
    #Function to return a list containing the union of the two arrays.
def findUnion(arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        arr3 = []
        i = 0
        j =  0
        
       
        while (i < (n))  and (j < (m)):
            if arr1[i] < arr2[j] :
                if len(arr3) == 0 or arr1[i] != arr3[-1]:
                    arr3.append(arr1[i])
                    
                    
                    
                i+=1
            elif arr1[i] > arr2[j] :
                if len(arr3) == 0 or arr1[j] != arr3[-1]:
                    arr3.append(arr2[j])
                    
                   
                    
                j+=1
            else :
                if len(arr3) == 0:
                    arr3.append(arr1[i])
                    i+=1
                    j+=1
                elif arr3[-1] == arr2[j]  or arr3[-1] == arr1[i]: 
                    i+=1
                    j+=1
                elif  arr2[j] == arr2[i]:
                    arr3.append(arr1[i])
                    i+=1
                    j+=1
                    
                
            
            
        while(i<(n)):
            if len(arr3) == 0 or arr3[-1] != arr1[i] :
                arr3.append(arr1[i])
                
            i+=1
            
        while(j<(m)):
            if len(arr3) == 0 or arr3[-1] != arr2[j]:
                arr3.append(arr2[j])
                
            j+=1       
            
        return arr3
    
    
    
print(findUnion([-4,-1,6,9,10],[-2,-1,3,5,11,14],5,6))
