def peakelement(nums):
    a = 0
    b = len(nums)-1
    while(a<=b):
        mid = (a+b)//2
        if nums[mid]< nums[mid+1]:
            return nums[mid+1]
        elif nums[mid]>nums[mid+1]:
            b = mid-1
            
            
nums = [1,2,3,1]      
print(peakelement(nums))