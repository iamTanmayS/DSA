def search(nums,target):
        s = 0
        e = len(nums)-1
        pos = -1
    
        while(s<=e):
            mid = (s+e)//2
            if nums[mid] == target:
                pos = mid
                return pos
            elif nums[mid]<=nums[s] :
                if target > nums[mid] and target <= nums[e]:
                    s = mid+1
                    
                else:
                    e = mid-1
            
            else:
                if target >= nums[s] and target < nums[mid]:
                    e = mid-1
                    
                else:
                    s = mid+1
                    
        return pos  
    
nums = [1,2,3,4,5,6,6,7,8]
target = 10

print(search(nums,target))