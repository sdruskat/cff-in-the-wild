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
            with open(os.path.join(datadir, file)) as f:
                # Try to parse the YAML, and if we can't, add to the
                # invalid file list
                try:
                    cff_file = yaml.safe_load(f)
                    if sanity_check(cff_file):
                        cff_data.append(cff_file)
                    else:
                        invalid_file.append(file)
                except:
                    invalid_file.append(file)
    return cff_data, invalid_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datadir', type=str, required=True, help='Directory in which CFF file are stored')
    args = parser.parse_args()
    cff_data, invalid_file = read_cff_files(args.datadir)