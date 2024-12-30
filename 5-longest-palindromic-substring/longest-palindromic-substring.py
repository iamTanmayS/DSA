class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s  # If the string is empty or has one character, it's the palindrome.

        def expand_around_center(left: int, right: int) -> str:
            # Expand the window as long as it is a palindrome.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        for i in range(len(s)):
            # Check for odd-length palindromes (single center).
            odd_palindrome = expand_around_center(i, i)
            # Check for even-length palindromes (two centers).
            even_palindrome = expand_around_center(i, i + 1)

            # Update the longest palindrome found so far.
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome
        