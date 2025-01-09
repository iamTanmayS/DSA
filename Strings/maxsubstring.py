def generate_substrings(number):
    # Convert the number to a string for substring processing
    s = str(number)
    n = len(s)
    substrings = []

    # Use two nested loops to extract substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])

    return substrings


# Example Usage
number = 123
result = generate_substrings(number)
print(result)