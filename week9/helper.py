"""
def print_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:  # prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:  # if the number is divisible by any number between 2 and itself, it's not prime
                    break
            else:
                print(num)

# Example usage:
print_primes(10, 20)
"""
def print_square(number):
    square = number ** 2
    print(f"The square of {number} is {square}")

# Get the number from the user
num = int(input("Enter a number: "))

# Call the function
print_square(num)
