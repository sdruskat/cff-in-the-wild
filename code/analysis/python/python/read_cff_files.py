#!/usr/bin/env python3
import os
import yaml
import argparse
import subprocess


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
            with open(os.path.join(datadir, file)) as f:
                # Try to parse the YAML, and if we can't, add to the
                # invalid YAML list
                try:
                    cff_file = yaml.safe_load(f)
                    if validate(datadir + '/' + file):
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
