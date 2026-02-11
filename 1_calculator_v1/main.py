#====================[ All Functions ]===================

def read_input():
    # Read a
    while True:
        try:
            a = float(input("\nEnter a value for a:\n>> ").strip())
            break
        except ValueError:
            print("\nPlease try again with a real number.")
            
    # Read the operation
    while True:
        op = input("\nChoose an operation (+, -, *, /):\n>> ").strip()
        if op in "+-*/":
            break
        print("\nOperation not recognized. Please try again.")
            
    # Read b
    while True:
        try:
            b = float(input("\nEnter a value for b:\n>> ").strip())
            if op == "/" and b == 0:
                print("\nDivision by zero is not allowed, choose another number.")
            else:
                break
        except ValueError:
            print("\nPlease try again with a real number.")
            
    return a, b, op


def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b
    elif op == "*":
        return a * b
    else:
        print("System error.")
        return None


#====================[ Main ]===================

def main():
    print("=== Welcome to the mini-calculator ===")
    
    while True:
        # Read values and operation
        a, b, op = read_input()
        
        # Calculate
        result = calculate(a, b, op)
        
        # Display
        print(f"\nResult: {a} {op} {b} = {result}")
        
        # Ask to continue
        again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for using the calculator. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
