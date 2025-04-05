import strings

def main():
    
    while True:
        print("Menu")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            dna1 = input("Enter first DNA string: ").upper()
            dna2 = input("Enter second DNA string: ").upper()
            
            try:
                distance = get_hamming_distance(dna1, dna2)
                print("Hamming Distance:", distance)
            
            except ValueError as e:
                print("Error:", e)
        
        elif choice == '2':
            dna = input("Enter DNA string: ").upper()
            
            try:
                complement = get_dna_complement(dna)
                print("DNA Complement:", complement)
            except ValueError as e:
                print("Error:", e)
        
        elif choice == '3':
            print("Goodbye! ")
            
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
