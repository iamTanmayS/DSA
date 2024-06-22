import math
 
n = int(input("enter the number"))
m = int(input("enter the exponent"))

#Approach 1#
 
'''
def computinpower(a,b):
    return math.pow(a,b)
    
    
print(computinpower(n,m))
    
'''
#Approach 2#

''' def computinpower(a,b):
    if b == 0:
        return 1
    elif b%2 == 0:
        return computinpower(a,b//2)*computinpower(a,b//2)
    else:
        return a*computinpower(a,b//2)*computinpower(a,b//2)
    
    
print(computinpower(n,m)) '''