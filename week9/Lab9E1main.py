
### YOUR CODE GOES BELOW
import sys

def calculate_net_salary(salary, tax_rate):
    return salary - (tax_rate * salary)

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <salary> <tax_rate>")
        return

    # Get the salary and tax rate from command line arguments
    try:
        salary = float(sys.argv[1])
        tax_rate = float(sys.argv[2])
    except ValueError:
        print("Please provide valid salary and tax rate.")
        return

    # Calculate the net salary
    net_salary = calculate_net_salary(salary, tax_rate)

    # Display the net salary
    print(f"Net Salary: {net_salary}")

if __name__ == "__main__":
    main()

### END CODE
