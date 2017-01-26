def distance(dna1, dna2):
    """ Returns the Hamming difference between 2 DNA Strands """
    if len(dna1) != len(dna2):
        raise ValueError

    dist = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            dist += 1

    return dist
