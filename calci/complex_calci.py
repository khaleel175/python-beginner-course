import cmath

def complex_calculator():
    print("Welcome to the Complex Number Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (mod)")
    print("6. Conjugate (conj)")
    print("7. Phase (phase)")
    print("8. Magnitude (abs)")
    
    while True:
        try:
            choice = input("\nEnter the operation number (or 'q' to quit): ").strip().lower()
            if choice == 'q':
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ['1', '2', '3', '4']:
                real1 = float(input("Enter the real part of the first number: "))
                imag1 = float(input("Enter the imaginary part of the first number: "))
                real2 = float(input("Enter the real part of the second number: "))
                imag2 = float(input("Enter the imaginary part of the second number: "))
                num1 = complex(real1, imag1)
                num2 = complex(real2, imag2)

                if choice == '1':
                    result = num1 + num2
                elif choice == '2':
                    result = num1 - num2
                elif choice == '3':
                    result = num1 * num2
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = num1 / num2

                print(f"The result is: {result}")

            elif choice == '5':
                real = float(input("Enter the real part of the number: "))
                imag = float(input("Enter the imaginary part of the number: "))
                num = complex(real, imag)
                result = abs(num)
                print(f"The modulus is: {result}")

            elif choice == '6':
                real = float(input("Enter the real part of the number: "))
                imag = float(input("Enter the imaginary part of the number: "))
                num = complex(real, imag)
                result = num.conjugate()
                print(f"The conjugate is: {result}")

            elif choice == '7':
                real = float(input("Enter the real part of the number: "))
                imag = float(input("Enter the imaginary part of the number: "))
                num = complex(real, imag)
                result = cmath.phase(num)
                print(f"The phase is: {result}")

            elif choice == '8':
                real = float(input("Enter the real part of the number: "))
                imag = float(input("Enter the imaginary part of the number: "))
                num = complex(real, imag)
                result = abs(num)
                print(f"The magnitude is: {result}")

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    complex_calculator()