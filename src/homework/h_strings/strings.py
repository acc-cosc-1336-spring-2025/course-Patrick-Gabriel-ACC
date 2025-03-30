def get_hamming_distance(dna1, dna2):

    if len(dna1) != len(dna2):

        raise ValueError("DNA sequences must be of equal length.")
    
    distance = 0

    index = 0

    while index < len(dna1):

        if dna1[index] != dna2[index]:

            distance += 1

        index += 1
    
    return distance

    print(distance)


def get_dna_complement(dna):
    complement = ''
    
    reversed_dna = dna[::-1]
    
    
    for base in reversed_dna:
        
        if base == 'A':
            complement += 'T'
        
        elif base == 'T':
            complement += 'A'
        
        elif base == 'C':
            complement += 'G'
        
        elif base == 'G':
            complement += 'C'
        
        else:
            
            raise ValueError("Invalid DNA base: " + base)
    
    return complement


    print(complement)