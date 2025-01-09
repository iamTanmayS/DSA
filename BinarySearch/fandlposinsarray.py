def searchRange(nums,target):
        s = 0
        e = len(nums)-1
        pos1 = -1
        pos2 = -1
        while(s<=e):
            mid = (s+e) //  2
            if len(nums) == 1 and nums[0] == target:
                pos1 = 0
                pos2 = 0
                return pos1,pos2
            if nums[mid] == target:
                if nums[mid-1] == target and len(nums)>2:
                    pos1 = mid-1
                    pos2 = mid
                    return pos1,pos2
                elif nums[mid+1] == target:
                    pos1 = mid
                    pos2 = mid+1
                    return pos1,pos2
                else: 
                    pos1 = mid
                    pos2 = mid
                    return pos1,pos2
                
                    return pos1,pos2
            if nums[mid]> target:
                e = mid-1
            else:
                s = mid+1
        return pos1,pos2


nums = [1,4]
target = 4
print(searchRange(nums,target))