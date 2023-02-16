from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences(path='data/jobs.csv', word='Python') == 1639
    assert count_ocurrences(path='data/jobs.csv', word='Javascript') == 122
