def recurbs(nums,tar,s,e):
    if s>e:
        return -1
    m = (s+e)//2
    
    if tar == nums[m]:
        return m
    elif tar>nums[m]:
        return recurbs(nums,tar,m+1,e)
    elif tar<nums[m]:
        return recurbs(nums,tar,s,m-1)
    
        
a = [3,43,2,32,4,668,675,6454,34,23] 
print(recurbs(a,3,0,len(a)-1))