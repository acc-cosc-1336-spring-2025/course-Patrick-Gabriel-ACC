from lists import get_p_distance_matrix

def main():
    
    while True:
        print("1 - Get p distance matrix")
        print("2 - Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Enter DNA sequences as comma-separated letters (e.g., T,T,T,C,C,A,T,T,T,A)")
            dna_list = []
            n = int(input("How many sequences? "))
            for i in range(n):
                sequence = input(f"Enter sequence {i + 1}: ").strip().split(',')
                dna_list.append(sequence)

            matrix = get_p_distance_matrix(dna_list)
            print("P-Distance Matrix:")
            for row in matrix:
                print(" ".join(f"{val:.5f}" for val in row))

        elif choice == "2":
            print("Exiting...")
            
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
