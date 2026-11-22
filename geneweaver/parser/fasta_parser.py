from Bio import SeqIO
from pathlib import Path


VALID_DNA_BASES = set("ACGTRYSWKMBDHVN")


def parse_fasta(file_path):
    """
    Read DNA sequences from a FASTA file.

    Args:
        file_path: Path to the FASTA file.

    Returns:
        A list of dictionaries containing sequence IDs and sequences.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or contains invalid DNA.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"FASTA file not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    records = []

    for record in SeqIO.parse(path, "fasta"):
        sequence_id = record.id
        sequence = str(record.seq).upper()

        if not sequence:
            raise ValueError(f"Empty DNA sequence: {sequence_id}")

        invalid_bases = set(sequence) - VALID_DNA_BASES

        if invalid_bases:
            raise ValueError(
                f"Invalid DNA bases in {sequence_id}: {invalid_bases}"
            )

        records.append({
            "id": sequence_id,
            "sequence": sequence
        })

    if not records:
        raise ValueError("FASTA file is empty or contains no valid records.")

    return records
