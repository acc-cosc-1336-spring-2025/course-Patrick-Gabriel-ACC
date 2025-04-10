def get_p_distance(list1, list2):
    differences = 0
    
    for a, b in zip(list1, list2):
        
        if a != b:
            differences += 1
    
    return differences / len(list1)


def get_p_distance_matrix(dna_list):
    n = len(dna_list)
    matrix = []
    
    for i in range(n):
        row = []
        
        for j in range(n):
            row.append(round(get_p_distance(dna_list[i], dna_list[j]), 5))
        matrix.append(row)
    
    return matrix
