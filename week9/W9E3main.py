

### YOUR CODE GOES BELOW
import sys

# Function to compute the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python W9E3main.py <number>")
    sys.exit(1)

# Get the number from command line argument
try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

# Compute factorial
result = factorial(number)

# Display the result
print(f"The factorial of {number} is: {result}")



### END CODE
