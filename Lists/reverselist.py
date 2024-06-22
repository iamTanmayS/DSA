#Approach 1#
def reverselist(n):
    n.reverse()
    return n

#Approach 2#

def reverselist2(n):
    n = n[::-1]
    return n

#Approach 3#

def reverselist3(n):
    for i in range(len(n)//2): 
        temp = n[i]
        n[i] = n[len(n)-i-1]
        n[len(n)-i-1] = temp
    return n
        
        
n = [1,2,3,4,5]
x = [2,5,2,5,3,5,1]
y = [2,6,1,4,7,4,9]
print("1",reverselist(n))
print("2",reverselist2(x))
print('3',reverselist3(y))