from geneweaver.processing.sequence_processor import (
    normalize_sequence,
    validate_dna_sequence,
    reverse_complement
)


def count_mismatches(guide: str, target: str) -> int:
    """
    Count the number of different positions between two DNA sequences.
    """

    if len(guide) != len(target):
        raise ValueError("Guide and target sequences must have equal lengths.")

    return sum(
        base1 != base2
        for base1, base2 in zip(guide, target)
    )


def align_sequence(
    guide: str,
    target: str,
    max_mismatches: int = 3
) -> list:
    """
    Find potential matching regions in a target DNA sequence.

    Searches both forward and reverse-complement strands.
    """

    guide = normalize_sequence(guide)
    target = normalize_sequence(target)

    validate_dna_sequence(guide)
    validate_dna_sequence(target)

    if not isinstance(max_mismatches, int) or isinstance(max_mismatches, bool):
        raise TypeError("max_mismatches must be an integer.")

    if max_mismatches < 0:
        raise ValueError("max_mismatches cannot be negative.")

    if len(guide) > len(target):
        return []

    results = []

    strands = {
        "forward": target,
        "reverse": reverse_complement(target)
    }

    for strand_name, sequence in strands.items():

        for i in range(len(sequence) - len(guide) + 1):

            window = sequence[i:i + len(guide)]

            mismatches = count_mismatches(guide, window)

            if mismatches <= max_mismatches:

                results.append({
                    "position": i,
                    "strand": strand_name,
                    "target": window,
                    "mismatches": mismatches
                })

    return results