### YOUR CODE GOES BELOW
import sys
import sorthelper

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2:
        print("Usage: python W9E5main.py <number1> <number2> ...")
        return

    # Get the numbers from command line arguments
    numbers = []
    for arg in sys.argv[1:]:
        try:
            numbers.append(float(arg))
        except ValueError:
            print("Please provide valid numbers.")
            return

    # Sort the numbers using the sortNumbers function from sorthelper.py
    sorted_numbers = sorthelper.sortNumbers(numbers)

    # Display the sorted numbers
    print("Sorted numbers:", sorted_numbers)

if __name__ == "__main__":
    main()


### END CODE
