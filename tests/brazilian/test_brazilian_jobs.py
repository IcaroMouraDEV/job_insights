from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert 'title' in result[0]
    assert 'salary' in result[0]
    assert 'type' in result[0]
