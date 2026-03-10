def get_number(prompt):
    """
    prompting user to enter a number, and it returns valid number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("PLease Enter a valid Number!")

def get_operator():
    """
    prompting user to enter a valid arithmetic operator 
    """
    valid_operators = ['+','-','*','/']
    
    while True:
        operator = input("Enter the operator: ")
        if operator in valid_operators:
            return operator
        else:
            print("Invalid Operator!")

def calculate(num1, num2, operator):
    """
    This function performs the Arithmetic calculations
    Take Args num1, num2, operator and returns the result of the calculation
    """
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        if num2 ==0:
            raise ZeroDivisionError('Divison by zero is not allowed.')
        return num1/num2
    
def main():
    """
    This is a main function to run the calculator program
    """
    print("Calculator App")

    num1 = get_number("Enter the First Number: ")
    operator = get_operator()
    num2 = get_number("Enter the Second Number: ")

    try:
        result = calculate(num1, num2, operator)
        print("Result: ", result)
    except ZeroDivisionError as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()