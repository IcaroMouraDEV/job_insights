from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            'title': 'Back end developer',
            'min_salary': 3000,
            'max_salary': 4000,
            'date_posted': '2022-04-12',
        },
        {
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 5000,
            'date_posted': '2022-08-12',
        },
        {
            'title': 'Web developer',
            'min_salary': 500,
            'max_salary': 1500,
            'date_posted': '2022-09-12',
        },
        {
            'title': 'Full stack developer',
            'min_salary': 4000,
            'max_salary': 8000,
            'date_posted': '2022-12-12',
        },
    ]
    expected_result = [
        {
            'title': 'Web developer',
            'min_salary': 500,
            'max_salary': 1500,
            'date_posted': '2022-09-12',
        },
        {
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 5000,
            'date_posted': '2022-08-12',
        },
        {
            'title': 'Back end developer',
            'min_salary': 3000,
            'max_salary': 4000,
            'date_posted': '2022-04-12',
        },
        {
            'title': 'Full stack developer',
            'min_salary': 4000,
            'max_salary': 8000,
            'date_posted': '2022-12-12',
        },
    ]

    sort_by(jobs, criteria='min_salary')

    assert jobs == expected_result

    expected_result = [
        {
            'title': 'Full stack developer',
            'min_salary': 4000,
            'max_salary': 8000,
            'date_posted': '2022-12-12',
        },
        {
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 5000,
            'date_posted': '2022-08-12',
        },
        {
            'title': 'Back end developer',
            'min_salary': 3000,
            'max_salary': 4000,
            'date_posted': '2022-04-12',
        },
        {
            'title': 'Web developer',
            'min_salary': 500,
            'max_salary': 1500,
            'date_posted': '2022-09-12',
        },
    ]

    sort_by(jobs, 'max_salary')

    assert jobs == expected_result

    expected_result = [
        {
            'title': 'Full stack developer',
            'min_salary': 4000,
            'max_salary': 8000,
            'date_posted': '2022-12-12',
        },
        {
            'title': 'Web developer',
            'min_salary': 500,
            'max_salary': 1500,
            'date_posted': '2022-09-12',
        },
        {
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 5000,
            'date_posted': '2022-08-12',
        },
        {
            'title': 'Back end developer',
            'min_salary': 3000,
            'max_salary': 4000,
            'date_posted': '2022-04-12',
        },
    ]

    sort_by(jobs, 'date_posted')

    assert jobs == expected_result
