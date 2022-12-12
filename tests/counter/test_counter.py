import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "trybe") == 0
    assert count_ocurrences("data/jobs.csv", "Javascript") == 122
    assert count_ocurrences("data/jobs.csv", "JAVASCRIPT") == 122
    # assert count_ocurrences("data/jobs.csv", "trybe") == 0
    with pytest.raises(FileNotFoundError):
        count_ocurrences("data/jobs.json", "java")
