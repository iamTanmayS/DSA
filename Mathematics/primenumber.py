
#Approach 1#

''' def prime():
    n = int(input("enter the number : "))
    count = 0
    for i in range(2,n):
        if (n % i == 0):
            count = count + 1
        
    if count == 0:
        print("Number is prime")
    else:
        print("Number is Composite") 
            
prime()  '''

#Approach 2#


def prime(a):
    
    count = 0
    for i in range(2,a):
        if (a % i == 0):
            count = count + 1
        
    if count == 0:
        return True
    else:
        return  False


         
        