def to_rna(dna):
    """ Returns RNA transcription of DNA string """
    dna_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    output = ''

    for i in dna:
        try:
            output += dna_rna[i]
        except KeyError:
            return ''

    return output
