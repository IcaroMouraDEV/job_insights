import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, encoding="utf-8") as file:
        jobs = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = jobs
        arr = []
        for index in range(len(data)):
            dict = {}
            for header_index in range(len(header)):
                dict[header[header_index]] = data[index][header_index]
            arr.append(dict)
        return arr


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    arr = set()
    for job in jobs:
        arr.add(job['job_type'])
    return arr


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    arr = []
    for job in jobs:
        if job['job_type'] == job_type:
            arr.append(job)
    return arr


# read('data/jobs.csv')
# get_unique_job_types('data/jobs.csv')
