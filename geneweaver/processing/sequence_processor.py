# Supported IUPAC DNA nucleotide symbols
VALID_DNA_BASES = set("ACGTRYSWKMBDHVN")


def normalize_sequence(sequence: str) -> str:
    """
    Remove whitespace and convert a DNA sequence to uppercase.
    """

    if not isinstance(sequence, str):
        raise TypeError("DNA sequence must be a string.")

    return "".join(sequence.split()).upper()


def validate_dna_sequence(sequence: str) -> bool:
    """
    Validate a DNA sequence using standard IUPAC nucleotide symbols.
    """

    sequence = normalize_sequence(sequence)

    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    invalid_bases = set(sequence) - VALID_DNA_BASES

    if invalid_bases:
        raise ValueError(
            f"Invalid DNA characters found: {invalid_bases}"
        )

    return True


def reverse_complement(sequence: str) -> str:
    """
    Generate the reverse complement of a DNA sequence.
    """

    sequence = normalize_sequence(sequence)

    validate_dna_sequence(sequence)

    complement_table = str.maketrans(
        "ATGCRYSWKMBDHVN",
        "TACGYRSWMKVHDBN"
    )

    return sequence.translate(complement_table)[::-1]