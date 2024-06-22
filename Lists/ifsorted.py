
#Approach 1#
def issorted(n):
    for i in range(1,len(n)):
        if n[i-1] > n[i]:
            return False
    return True

#Approach 2#

def issorted2(n):
    sl = sorted(n)
    if sl == n:
        return True
    else:
        return False
    
n = [1,2,2,2,2]
print(issorted(n))
print(issorted2(n))