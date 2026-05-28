"""Transcribe a DNA strand into its RNA complement."""
def to_rna(dna_strand):
    """RNA are adenine (A), cytosine (C), guanine (G), and uracil (U)."""
    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))