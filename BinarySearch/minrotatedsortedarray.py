def findMin(nums):
        s = 0
        e = len(nums)-1
        while(s<e):
            m = (s+e)//2
            if nums[m]>nums[e]:
                s=m+1
            else:
                e=m
        return nums[s] 
    

nums = [4,5,6,7,0,1,2]
print(findMin(nums))