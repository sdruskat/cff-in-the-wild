from python.calculate_stats import created_with_cffinit
"""Tests for the calculate_tests.py file"""


def test_created_by_cffinit():
    """Test the function that returns the number of
    files created by CFF by passing it some dummy
    data."""
    created_by_cffinit = {
        'created_by_cffinit': True
    }
    not_created_by_cffinit = {
        'created_by_cffinit': False
    }
    n_cffinit = created_with_cffinit([
        created_by_cffinit,
        not_created_by_cffinit
    ])
    assert n_cffinit == 1