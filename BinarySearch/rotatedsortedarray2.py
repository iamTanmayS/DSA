def search(nums,target):
        s =  0
        e = len(nums)-1
        l = 0
        r = 0
        while (s<=e):
            mid = (s+e)//2
            if nums[mid] == target:
                return True
            elif nums[mid]>nums[s]:
                if target<nums[mid] and target>=nums[s]:
                    e = mid-1
                else:
                    s = mid+1
            else:
                if target>nums[mid] and target<= nums[e]:
                    s = mid+1
                else:
                    e = mid-1
        return False

nums = [7,9,11,1,3,5]
target = 3
print(search(nums,target))


        