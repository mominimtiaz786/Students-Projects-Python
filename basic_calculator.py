import math

def add(x, y):
    # This function adds two numbers and returns the result.
    return x + y

def subtract(x, y):
    # This function subtracts two numbers and returns the result.
    return x - y

def multiply(x, y):
    # This function multiplies two numbers and returns the result.
    return x * y

def divide(x, y):
    # This function divides two numbers and returns the result.
    # It also handles the case where y is 0 and prints an error message.
    if y == 0:
        print('Error: division by zero')
        return None
    return x / y

def square_root(x):
    # This function calculates the square root of a number and returns the result.
    return math.sqrt(x)

def is_prime_number(x):
    # This function checks if a number is prime and returns a Boolean value indicating the result.
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_square(x):
    # This function calculates the square of a number and returns the result.
    return x ** 2

def get_cube(x):
    # This function calculates the cube of a number and returns the result.
    return x ** 3

def main():
    # This is the main function of the calculator.
    # It prompts the user for two numbers and an operator, and then performs the specified operation on the numbers.
    # It also handles the case where the operator is 'sqrt', 'prime', 'square', or 'cube', and calls the appropriate function.
    # It prints the result of the operation.
    x = float(input('Enter the first number: '))
    y = float(input('Enter the second number: '))
    operator = input('Enter an operator (+, -, *, /, sqrt, prime, square, cube): ')
    result = None
    if operator == '+':
        result = add(x, y)
    elif operator == '-':
        result = subtract(x, y)
    elif operator == '*':
        result = multiply(x, y)
    elif operator == '/':
        result = divide(x, y)
    elif operator == 'sqrt':
        result = square_root(x)
    elif operator == 'prime':
        result = is_prime_number(x)
    elif operator == 'square':
        result = get_square(x)
    elif operator == 'cube':
        result = get_cube(x)
    else:
        print('Error: invalid operator')
    if result is not None:
        print(f'Result: {result}')

if __name__ == '__main__':
    # This block is executed when the program is run.
    # It calls the main() function.
    main()
