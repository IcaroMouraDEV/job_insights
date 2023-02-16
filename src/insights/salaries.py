from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    # https://www.w3schools.com/python/ref_string_isdigit.asp
    max_salary = {
        int(job['max_salary']) for job in jobs if job['max_salary'].isdigit()
    }
    return max(max_salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    # https://www.w3schools.com/python/ref_string_isdigit.asp
    min_salary = {
        int(job['min_salary']) for job in jobs if job['min_salary'].isdigit()
    }
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError

    validate([job['min_salary'], job['max_salary'], salary])

    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def validate(
    salaries: List[Union[int, str]]
) -> None:

    is_str_or_int_salaries = [
        type(value) in (int, str) for value in salaries
    ]

    is_valid_str_salaries = [
        value.isnumeric() for value in salaries if isinstance(value, str)
    ]

    if not all(is_str_or_int_salaries) or not all(is_valid_str_salaries):
        raise ValueError

    if int(salaries[0]) > int(salaries[1]):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            continue
    return filtered_jobs


# get_max_salary('data/jobs.csv')
# get_min_salary('data/jobs.csv')
