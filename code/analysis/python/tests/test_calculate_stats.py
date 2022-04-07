from python.calculate_stats import created_with_cffinit, which_cff_version
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


def test_which_cff_version():
    """Test the function that outputs the number
    of CFF files with each version"""
    v111 = { 'cff-version': '1.1.1' }
    v112 = { 'cff-version': '1.1.2' }
    cff_data = [v111, v111, v112]
    cff_version = which_cff_version(cff_data)
    assert cff_version['1.1.1'] == 2
    assert cff_version['1.1.2'] == 1