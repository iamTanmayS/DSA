class Solution:
    def maxScore(self, s: str) -> int:
        # Count total number of '1's in the string
        total_ones = s.count('1')
        current_zeros = 0
        right_ones = total_ones
        max_score = float('-inf')  # Initialize max_score to negative infinity

        # Iterate through the string, excluding the last character for split
        for i in range(len(s) - 1):
            if s[i] == '0':
                current_zeros += 1
            else:
                right_ones -= 1
            
            # Calculate the current score
            current_score = current_zeros + right_ones
            
            # Update max_score
            max_score = max(max_score, current_score)
        
        return max_score
