def bs(nums,t):
    s = 0
    end = len(nums)
    k =0
    mid = (s+end)//2
    while(s<=end):
        if (t == nums[mid]):
            k = 1
            break
        elif(t>nums[mid]):
            s = mid+1
        elif(t<nums[mid]):
            end = mid-1
        
    if k != 1:
        print("NOT")
    if k == 1 : 
        print(f"found at {mid}")
            
            
bs([2,3,53,32,3,21,4,65,65,343,4,2312,21,2],65)