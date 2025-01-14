class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create frequency dictionaries for both strings
        freq_s = {}
        freq_t = {}
        
        # Count character frequencies for s
        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1
        
        # Count character frequencies for t
        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1
        
        # Compare both dictionaries
        for key in freq_s:
            if freq_s.get(key, 0) != freq_t.get(key, 0):
                return False
        
        # Ensure no extra characters in t
        for key in freq_t:
            if freq_t.get(key, 0) != freq_s.get(key, 0):
                return False
        
        return True
