#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 10
#   References: no one
#   Time: 2 hours

def dna_to_rna(sequence):
    rna_sequence = ""
    for letter in sequence:
        if letter == "A":
            rna_sequence += "U"
        elif letter == "T":
            rna_sequence += "A"
        elif letter == "G":
            rna_sequence += "C"
        elif letter == "C":
            rna_sequence += "G"
    return rna_sequence


def parse_file_into_acids(filename):
    amino_acids = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 4:
                amino_acids.append(parts)
    return amino_acids


def finding_protein_sequence(codons_file, dna_sequence):
    rna_sequence = dna_to_rna(dna_sequence)
    amino_acids = parse_file_into_acids(codons_file)
    start_codon_index = rna_sequence.find("AUG")
    rna_sequence = rna_sequence[start_codon_index:]
    protein_sequence = []
    codon_length = 3
    stop_codons = ["UAA", "UGA", "UAG"]
    found_stop_codon = False

    for i in range(0, len(rna_sequence), codon_length):
        codon = rna_sequence[i:i + codon_length]
        protein_sequence.append(codon)
        if codon in stop_codons:
            found_stop_codon = True
            break

    if found_stop_codon:
        stop_codon_index = protein_sequence.index(codon)
        protein_sequence = protein_sequence[:stop_codon_index]

    final_protein = ""
    for codon in protein_sequence:
        for amino_acid in amino_acids:
            if codon in amino_acid:
                final_protein += amino_acid[2]
                break
            if codon in stop_codons:
                break

    return final_protein


def test_dna_to_rna(DNA, expected_RNA):
    result = dna_to_rna(DNA)
    assert result == expected_RNA


def test_parse_file_into_acids(file, expected_output):
    result = parse_file_into_acids(file)
    assert result == expected_output


def test_finding_protein_sequence(file, given_dna, expected_proteins):
    result = finding_protein_sequence(file, given_dna)
    assert result == expected_proteins


def test_my_functions():
    test_dna_to_rna("A", "U")
    test_dna_to_rna("CGTAAGCT", "GCAUUCGA")
    test_dna_to_rna("T", "A")
    test_finding_protein_sequence("codons.txt", "TTAAACCGGGCCCGGCTACCGACCCATGATTAAACCCTACTCAAATCATT", "MAGY")
    test_finding_protein_sequence("codons.txt", "ATTTAAGGGCTACCCAATGATGTTTTTAACGCCCACTGCGGCAAA", "MGYYKNCG")
    test_finding_protein_sequence("codons.txt", "ATATCGCGACGTACAGTGCAGTCTAGGTCACGATCCCATGTG", "MSRQIQC")
    test_finding_protein_sequence("codons.txt", "ATATCGCGACGTACAGGTGCGCCCGCCCTGTAGATGGATAGAGACAGTGTACTATCCCATGTG", "MSTRAGHLPISVT")


def main():
    codons_file = input("FILE NAME> ")
    dna_sequence = input("SEQUENCE> ")
    protein_acronym = finding_protein_sequence(codons_file, dna_sequence)
    print(f"OUTPUT {protein_acronym}")
    test_my_functions()


if __name__ == "__main__":
    main()
