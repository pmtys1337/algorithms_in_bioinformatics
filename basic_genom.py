def read_genome(filename):
    genome = ""
    with open(filename) as file:
        for line in file:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

def reverse_complement(chain):
    complement={"A": "T",
                "T": "A",
                "C": "G",
                "G": "C"}
    rev_chain_complement = ""
    for base in chain:
        rev_chain_complement = complement[base] + rev_chain_complement
    return rev_chain_complement

def naive_match(word, text):
    assert len(word) <= len(text)
    occurences = []
    for i in range(0,len(text)-len(word)+1):
        match = True
        for j in range(0, len(word)):
            if word[j] != text[i+j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences
