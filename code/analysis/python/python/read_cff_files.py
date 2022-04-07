#!/usr/bin/env python3
import os
import yaml
import argparse
import subprocess

from calculate_stats import which_cff_version


def validate(infile):
    output = subprocess.check_output(['cffconvert', '--validate', '-i', infile])
    return b'Citation metadata are valid according to schema version' in output


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
                f.seek(0)
                # Try to parse the YAML, and if we can't, add to the
                # invalid YAML list
                try:
                    cff_file = yaml.safe_load(f)
                    if validate(os.path.join(datadir, file)):
                        # Was the file created by CFFinit? Relies on this comment
                        # being on the first line
                        if 'This CITATION.cff file was generated with cffinit' in cff_str:
                            cff_file['created_by_cffinit'] = True
                        else:
                            cff_file['created_by_cffinit'] = False
                        _cff_data.append(cff_file)
                    else:
                        # Invalid CFF, but valid YAML
                        _invalid_cff.append(file)
                except:
                    _invalid_yaml.append(file)
    return _cff_data, _invalid_cff, _invalid_yaml


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datadir', type=str, required=True, help='Directory in which CFF file are stored')
    args = parser.parse_args()

    cff_data, invalid_cff, invalid_yaml = read_cff_files(args.datadir)

    print(f'CFF files: {len(cff_data)}')
    print(f'Invalid CFF files: {len(invalid_cff)}')
    print(f'Invalid YAML files: {len(invalid_yaml)}')

    # Check how many were created using CFFinit
    cffinit = 0
    for cff in cff_data:
        if cff['created_by_cffinit']:
            cffinit = cffinit + 1
    print(f'Files created with CFFinit: {cffinit}')

    # Which CFF versions
    cff_versions = which_cff_version(cff_data)
    print('CFF versions: ', cff_versions)
