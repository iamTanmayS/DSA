def searchInsert(nums,target):
        s = 0
        end = len(nums)-1
        pos = -1
        while(s<=end):
            mid = (s+end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                s = mid+1
                pos = mid
            else:
                end = mid-1
        return pos+1
    
    
    
nums = [1,3,4,5,6,7,8]
target = 2
print(searchInsert(nums,target))