from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "trybe") == 0
    # assert count_ocurrences("data/jobs.csv", "") == 0
