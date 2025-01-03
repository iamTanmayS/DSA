class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Compute the total sum of the array
        prefix_sum = 0         # Initialize prefix sum
        valid_count = 0        # Count of valid splits

        # Iterate through the array up to the second-to-last element
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]  # Update the prefix sum
            suffix_sum = total_sum - prefix_sum  # Compute the suffix sum
            if prefix_sum >= suffix_sum:  # Check if the split is valid
                valid_count += 1

        return valid_count  # Return the number of valid splits
   