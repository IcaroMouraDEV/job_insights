from src.pre_built.sorting import sort_by
from src.insights.jobs import read

def test_sort_by_criteria():
    jobs = read('tests/mocks/jobs_sorting.csv')
    
    sort_by(jobs, criteria='min_salary')

    assert jobs[0]['min_salary'] == '500'
    assert jobs[1]['min_salary'] == '1000'
