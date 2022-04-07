from pathlib import Path
import csv

"""Creates a CSV file from the initial hack day raw data.
It has two columns ('org' and 'name') that contain the result of retrieving this info from the files names,
which have the pattern <org>_<name>_CITATION.cff."""


def run():
    """Go through all files in the raw data directory,
    split their names into GitHub org and name,
    and write them to a CSV file in the data directory."""
    data_dir = '../../data/' 
    raw_dir = data_dir + 'raw/'
    pathlist = Path(raw_dir).glob('*.cff')
    with open(data_dir + 'cff_repositories.csv', 'w') as outfile:
        of_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        of_writer.writerow(['org','name'])
        for path in pathlist:
            path_in_str = str(path)
            filename = path_in_str.split('/')[-1]
            split = filename.split('_')
            org = split[0]
            name = split[1]
            of_writer.writerow([org,name])


if __name__ == '__main__':
    run()
