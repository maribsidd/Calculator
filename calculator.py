"""
Simple Calculator
A command-line calculator that performs basic arithmetic operations
"""

print("=" * 50)
print("SIMPLE CALCULATOR")
print("=" * 50)
print()

while True:
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print()
    
    ch = input("Enter choice (1-5): ")
    
    if ch == '5':
        print("Thank you for using calculator!")
        break
    
    if ch in ['1', '2', '3', '4']:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        
        if ch == '1':
            r = n1 + n2
            print(f"Result: {n1} + {n2} = {r}")
        elif ch == '2':
            r = n1 - n2
            print(f"Result: {n1} - {n2} = {r}")
        elif ch == '3':
            r = n1 * n2
            print(f"Result: {n1} × {n2} = {r}")
        elif ch == '4':
            if n2 != 0:
                r = n1 / n2
                print(f"Result: {n1} ÷ {n2} = {r}")
            else:
                print("Error: Division by zero!")
    else:
        print("Invalid choice! Please enter 1-5.")
    
    print()
    print("-" * 50)
    print()
