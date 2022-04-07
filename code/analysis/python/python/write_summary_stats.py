#!/usr/bin/env python3
"""Functions to write summary stats to file."""
import os
import argparse
from read_cff_files import read_cff_files
import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datadir', type=str, required=True, help='Directory in which CFF file are stored')
    args = parser.parse_args()

    currentdir = os.path.dirname(os.path.abspath(__file__))

    # Get the file counts
    cff_data, invalid_cff, invalid_yaml = read_cff_files(args.datadir)
    # Numbers of files
    df = pd.DataFrame(data={'descriptor': ['Valid CFF files', 'Invalid CFF files', 'Invalid YAML files'],
                            'count': [len(cff_data), len(invalid_cff), len(invalid_yaml)]})
    df.to_csv(os.path.join(currentdir, '../../../../data/analysed/file_counts.csv'))

