import pytest

from geneweaver.alignment.cpu_aligner import (
    count_mismatches,
    align_sequence
)


def test_count_mismatches():
    assert count_mismatches("ATGC", "AAGC") == 1


def test_count_mismatches_no_difference():
    assert count_mismatches("ATGC", "ATGC") == 0


def test_count_mismatches_different_lengths():
    with pytest.raises(ValueError):
        count_mismatches("ATGC", "ATG")


def test_forward_exact_match():
    results = align_sequence("ATGC", "TTATGCAA", 0)

    assert any(
        result["strand"] == "forward"
        and result["target"] == "ATGC"
        and result["mismatches"] == 0
        for result in results
    )


def test_reverse_strand_match():
    results = align_sequence("ATGC", "GCAT", 0)

    assert any(
        result["strand"] == "reverse"
        and result["target"] == "ATGC"
        and result["mismatches"] == 0
        for result in results
    )


def test_alignment_with_one_mismatch():
    results = align_sequence("ATGC", "ATCC", 1)

    assert any(
        result["mismatches"] == 1
        for result in results
    )


def test_no_match_with_zero_mismatches():
    results = align_sequence("ATGC", "AAAA", 0)

    assert results == []


def test_guide_longer_than_target():
    results = align_sequence("ATGCA", "ATGC", 2)

    assert results == []


def test_invalid_dna_sequence():
    with pytest.raises(ValueError):
        align_sequence("ATGX", "ATGC")


def test_negative_mismatch_limit():
    with pytest.raises(ValueError):
        align_sequence("ATGC", "ATGC", -1)


def test_non_integer_mismatch_limit():
    with pytest.raises(TypeError):
        align_sequence("ATGC", "ATGC", 1.5)


def test_empty_guide():
    with pytest.raises(ValueError):
        align_sequence("", "ATGC")