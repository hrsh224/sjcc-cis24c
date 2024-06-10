
### YOUR CODE to set up the main function GOES BELOW
import sys
import helper

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <number1> <number2>")
        return

    # Get the numbers from command line arguments
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        return

    # Add the numbers using the add function from helper.py
    result = helper.add(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

### END CODE
