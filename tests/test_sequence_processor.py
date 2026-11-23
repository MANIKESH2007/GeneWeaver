import pytest

from geneweaver.processing.sequence_processor import (
    normalize_sequence,
    validate_dna_sequence,
    reverse_complement,
)


def test_normalize_lowercase_sequence():
    assert normalize_sequence("atgc") == "ATGC"


def test_remove_whitespace():
    assert normalize_sequence("atgc atga\ncc") == "ATGCATGACC"


def test_validate_valid_sequence():
    assert validate_dna_sequence("ATGCN") is True


def test_validate_iupac_sequence():
    assert validate_dna_sequence("ACGTRYSWKMBDHVN") is True


def test_invalid_dna_character():
    with pytest.raises(ValueError, match="Invalid DNA characters"):
        validate_dna_sequence("ATGX")


def test_empty_sequence():
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_dna_sequence("")


def test_non_string_input():
    with pytest.raises(TypeError, match="must be a string"):
        normalize_sequence(123)


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_reverse_complement_lowercase():
    assert reverse_complement("atgc") == "GCAT"


def test_reverse_complement_iupac():
    assert reverse_complement("ACGTRYSWKMBDHVN") == "NBDHVKMWSRYACGT"


def test_reverse_complement_empty_sequence():
    with pytest.raises(ValueError, match="cannot be empty"):
        reverse_complement("")