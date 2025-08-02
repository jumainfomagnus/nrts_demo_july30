#!/usr/bin/env python3
"""
Simple Calculator App
A command-line calculator that performs basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract second number from first number."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide first number by second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    """Get a valid operation from user input."""
    operations = {
        '+': ('addition', add),
        '-': ('subtraction', subtract),
        '*': ('multiplication', multiply),
        '/': ('division', divide)
    }
    
    print("\nAvailable operations:")
    for op, (name, _) in operations.items():
        print(f"  {op} - {name}")
    
    while True:
        operation = input("\nEnter operation (+, -, *, /): ").strip()
        if operation in operations:
            return operation, operations[operation]
        else:
            print("Invalid operation! Please choose +, -, *, or /")

def main():
    """Main calculator function."""
    print("=" * 40)
    print("     SIMPLE CALCULATOR")
    print("=" * 40)
    print("Welcome! This calculator performs basic arithmetic operations.")
    
    while True:
        try:
            # Get operation
            operation_symbol, (operation_name, operation_func) = get_operation()
            
            # Get numbers
            num1 = get_number(f"\nEnter first number: ")
            num2 = get_number(f"Enter second number: ")
            
            # Perform calculation
            result = operation_func(num1, num2)
            
            # Display result
            print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")
            
        except ValueError as e:
            print(f"\nError: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")
        
        # Ask if user wants to continue
        print("\n" + "-" * 40)
        continue_calc = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if continue_calc not in ['y', 'yes']:
            print("Thank you for using the calculator. Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()