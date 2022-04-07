#!/usr/bin/env python3
import os
import yaml
import argparse
from calculate_stats import which_cff_version


def read_cff_files(datadir):
    """Read CFF files from a directory and return a list of valid
    YAML CFF data and list of invalid YAML filenames"""
    cff_data = []
    invalid_file = []
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
                # invalid file list
                try:
                    cff_file = yaml.safe_load(f)
                    # Was the file created by CFFinit? Relies on this comment
                    # being on the first line
                    if 'This CITATION.cff file was generated with cffinit' in cff_str:
                        cff_file['created_by_cffinit'] = True
                    else:
                        cff_file['created_by_cffinit'] = False
                    cff_data.append(cff_file)
                except:
                    invalid_file.append(file)
    return cff_data, invalid_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datadir', type=str, required=True, help='Directory in which CFF file are stored')
    args = parser.parse_args()

    # Read the CFF files and print how many are valid YAML
    cff_data, invalid_files = read_cff_files(args.datadir)
    print(f'CFF files: {len(cff_data)}')
    print(f'Invalid files: {len(invalid_files)}')

    # Check how many were created using CFFinit
    cffinit = 0
    for cff in cff_data:
        if cff['created_by_cffinit']:
            cffinit = cffinit + 1
    print(f'Files created with CFFinit: {cffinit}')

    # Which CFF versions
    cff_versions = which_cff_version(cff_data)
    print('CFF versions: ', cff_versions)