import pytest
from pathlib import Path

from geneweaver.parser.fasta_parser import parse_fasta


def test_parse_multiple_sequences(tmp_path):
    fasta_file = tmp_path / "sample.fasta"

    fasta_file.write_text(
        ">seq1\nATGC\n>seq2\nGCTA\n"
    )

    result = parse_fasta(fasta_file)

    assert len(result) == 2
    assert result[0] == {"id": "seq1", "sequence": "ATGC"}
    assert result[1] == {"id": "seq2", "sequence": "GCTA"}


def test_convert_lowercase_to_uppercase(tmp_path):
    fasta_file = tmp_path / "lowercase.fasta"

    fasta_file.write_text(">seq1\natgc\n")

    result = parse_fasta(fasta_file)

    assert result[0]["sequence"] == "ATGC"


def test_invalid_dna_character(tmp_path):
    fasta_file = tmp_path / "invalid.fasta"

    fasta_file.write_text(">seq1\nATGX\n")

    with pytest.raises(ValueError, match="Invalid DNA bases"):
        parse_fasta(fasta_file)


def test_empty_fasta_file(tmp_path):
    fasta_file = tmp_path / "empty.fasta"
    fasta_file.write_text("")

    with pytest.raises(ValueError, match="FASTA file is empty"):
        parse_fasta(fasta_file)


def test_missing_fasta_file(tmp_path):
    fasta_file = tmp_path / "missing.fasta"

    with pytest.raises(FileNotFoundError):
        parse_fasta(fasta_file)


def test_empty_sequence(tmp_path):
    fasta_file = tmp_path / "empty_sequence.fasta"

    fasta_file.write_text(">seq1\n>seq2\nATGC\n")

    with pytest.raises(ValueError, match="Empty DNA sequence"):
        parse_fasta(fasta_file)


def test_iupac_ambiguity_codes(tmp_path):
    fasta_file = tmp_path / "ambiguity.fasta"

    fasta_file.write_text(">seq1\nACGTRYSWKMBDHVN\n")

    result = parse_fasta(fasta_file)

    assert result[0]["sequence"] == "ACGTRYSWKMBDHVN"