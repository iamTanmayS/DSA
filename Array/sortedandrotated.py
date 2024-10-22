
def check(nums):
        a = nums[:]
        flag = 0
        for i in range(len(nums)-1):
            min = i
            for j in range(i+1,len(nums)):
                if a[j]<a[min]:
                    min = j
            a[i],a[min] = a[min],a[i]
        sorted  = a[:]
        

        for j in range(len(nums)):
            temp = nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i]=nums[i-1]
            nums[0] = temp
            if nums == sorted :
                return True
        
        return False
        
        
        
print(check([3,4,5,1,2]))