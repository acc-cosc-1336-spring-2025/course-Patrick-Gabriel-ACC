import repetition

from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers

def main():
    while True:
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                while True:
                    num = int(input("Enter a number (greater than 0 and less than 10): "))
                    if 0 < num < 10:
                        print(f"Factorial of {num} is {get_factorial(num)}")
                        break
                    else:
                        print("Invalid input! Please enter a number between 1 and 9.")

            elif choice == 2:
                while True:
                    num = int(input("Enter a number (greater than 0 and less than 100): "))
                    if 0 < num < 100:
                        print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(num)}")
                        break
                    else:
                        print("Invalid input! Please enter a number between 1 and 99.")

            elif choice == 3:
                print("Exiting program. Goodbye!")
                break

            exit_choice = input("Do you want to exit? (y/n): ")
            if exit_choice == 'y':
                print("Exiting program. Goodbye!")
                break
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
