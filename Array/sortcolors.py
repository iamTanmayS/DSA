class Solution:
    def sortColors(self, nums):

        for i in range(len(nums)):
            flag = 0 
            for j in range(len(nums) - 1 - i):
                if nums[j]>nums[1+j]:
                    nums[j], nums[j+1]  = nums[j+1] ,nums[j]
                    flag= 1
            if flag==0:
                break
            