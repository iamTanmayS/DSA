def missingNumber(nums):
        a = len(nums)
        x = "y"
        nums.sort()
        for i in range(len(nums)):
            if  i != nums[i]:
                x = i
                break
        
        if x =="y":
            return len(nums)
        else:
            return x 
print(missingNumber([1,2]))