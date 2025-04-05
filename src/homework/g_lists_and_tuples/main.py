from lists import get_lowest_list_value, get_highest_list_value

def main():
    
    while True:
        print("Menu:")
        print("1 - Show the list low / high values")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            values = []
            
            while True:
                
                try:
                    num = int(input("Enter a list value: "))
                    values.append(num)

                    if len(values) >= 3:
                        more = input("Do you want to enter another value? (y/n): ")
                        
                        if more.lower() != 'y':
                            break
                
                except ValueError:
                    print("Please enter a valid number.")

            low = get_lowest_list_value(values)
            high = get_highest_list_value(values)
            print(f"Lowest value: {low}")
            print(f"Highest value: {high}")

        elif choice == "2":
            print("Goodbye!")
            
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()