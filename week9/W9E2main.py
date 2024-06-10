
### YOUR CODE GOES
# Function to compute the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Given number
number = 5  # You can change this number to compute factorial for a different number

# Compute factorial
result = factorial(number)

# Display the result
print(f"The factorial of {number} is: {result}")


### END CODE
