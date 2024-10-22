def zero(nums):
    total_zeros = nums.count(0)  # Total number of zeros in the array
    shifted_zeros = 0  # Keep track of shifted zeros
    i = 0

    while i <= len(nums) - 1 and shifted_zeros < total_zeros:
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                nums[j - 1] = nums[j]
            # Place 0 at the end
            nums[len(nums) - 1] = 0
            shifted_zeros += 1  # Increment the shifted zero count
        else:
            i += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
zero(nums)
print(nums) 