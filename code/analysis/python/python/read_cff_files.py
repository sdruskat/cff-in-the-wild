#!/usr/bin/env python3
import os
import yaml
import argparse


def sanity_check(cff_file: dict) -> bool:
    """Checks if the required keys for CFF exist in the given file.

    :param cff_file: A dictionary containing the metadata from a CFF file
    :return: whether the required keys for CFF exist in the file
    """
    return all(k in cff_file for k in ('cff-version', 'message', 'title', 'authors'))


def read_cff_files(datadir: str):
    """Read CFF files from a directory and return a list of valid
    YAML CFF data, a list of invalid CFF filenames,
    and a list of invalid YAML filenames"""
    _cff_data = []
    _invalid_yaml = []
    _invalid_cff = []
    # Loop over all of the files in the directory
    for file in os.listdir(datadir):
        # Check it's a .cff file
        if file.endswith('.cff'):
            # Open the file, read the YAML and append to cff_data
            with open(os.path.join(datadir, file), encoding='latin-1') as f:
                # Read the first line, which should contain the comment
                # saying it was created with CFFinit, if it was
                cff_str = f.readline()
                # Try to parse the YAML, and if we can't, add to the
                # invalid YAML list
                try:
                    cff_file = yaml.safe_load(f)
                    
                    if sanity_check(cff_file):
                        # Was the file created by CFFinit? Relies on this comment
                        # being on the first line
                        if 'This CITATION.cff file was generated with cffinit' in cff_str:
                            cff_file['created_by_cffinit'] = True
                        else:
                            cff_file['created_by_cffinit'] = False
                            
                        _cff_data.append(cff_file)
                    else:
                        # Invalid CFF, but valid YAML
                        _invalid_cff.append(file)cff_data.append(cff_file)
                except:
                    _invalid_yaml.append(file)
    return _cff_data, _invalid_cff, _invalid_yaml


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datadir', type=str, required=True, help='Directory in which CFF file are stored')
    args = parser.parse_args()

    cff_data, invalid_cff, invalid_yaml = read_cff_files(args.datadir)

    print(f'CFF files: {len(cff_data)}')
    print(f'Invalid files: {len(invalid_files)}')

    # Check how many were created using CFFinit
    cffinit = 0
    for cff in cff_data:
        if cff['created_by_cffinit']:
            cffinit = cffinit + 1
    print(f'Files created with CFFinit: {cffinit}')
