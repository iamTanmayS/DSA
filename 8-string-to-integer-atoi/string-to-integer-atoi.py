class Solution:
    def myAtoi(self, s: str) -> int:
        loop_var = 0
        length_s = len(s)
        newstring = ""
        sign = 1

        # Skip leading whitespaces
        while loop_var < length_s and s[loop_var] == " ":
            loop_var += 1

        # Check for sign
        if loop_var < length_s and (s[loop_var] == "-" or s[loop_var] == "+"):
            if s[loop_var] == "-":
                sign = -1
            loop_var += 1

        # Read digits and stop at non-digit
        while loop_var < length_s and "0" <= s[loop_var] <= "9":
            newstring += s[loop_var]
            loop_var += 1

        # If no digits were found
        if not newstring:
            return 0

        # Convert to integer and apply sign
        result = sign * int(newstring)

        # Clamp result to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result
