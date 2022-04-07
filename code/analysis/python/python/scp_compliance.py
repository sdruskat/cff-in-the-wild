import argparse

# import pandas as pd

from .read_cff_files import read_cff_files


def find_doi(cff):
    if cff is None:
        return

    if "doi" in cff:
        return cff["doi"]

    if "identifiers" in cff:
        identifiers = cff["identifiers"]
        found = None
        for i in identifiers:
            if "type" in i and i["type"] == "doi":
                found = i["value"]
                break
        return found


def compile_compliance(cff_data):
    sample_size = 0
    has_version_count = 0
    has_code_repo_count = 0
    has_doi_count = 0
    has_citation_count = 0
    is_compliant_count = 0

    for cff in cff_data:
        if cff is None:
            continue

        sample_size += 1

        has_version = "version" in cff
        has_code_repo = "repository-code" in cff
        has_doi = find_doi(cff) is not None
        has_citation = "preferred-citation" in cff

        is_compliant = has_version and has_code_repo and has_doi and has_citation

        has_version_count += int(has_version)
        has_code_repo_count += int(has_code_repo)
        has_doi_count += int(has_doi)
        has_citation_count += int(has_citation)
        is_compliant_count += int(is_compliant)

    print(f"Sample size:  {sample_size}")
    print(
        f"Has version:  {has_version_count} ({100*has_version_count/sample_size:.1f}%)"
    )
    print(
        f"Has repo:     {has_code_repo_count} ({100*has_code_repo_count/sample_size:.1f}%)"
    )
    print(f"Has DOI:      {has_doi_count} ({100*has_doi_count/sample_size:.1f}%)")
    print(
        f"Has citation: {has_citation_count} ({100*has_citation_count/sample_size:.1f}%)"
    )
    print(
        f"Compliant:    {is_compliant_count} ({100*is_compliant_count/sample_size:.1f}%)"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--datadir",
        type=str,
        required=True,
        help="Directory in which CFF file are stored",
    )
    args = parser.parse_args()

    cff_data, _, _ = read_cff_files(args.datadir)

    print(f"{len(cff_data)} valid files read")
    print()

    compile_compliance(cff_data)


if __name__ == "__main__":
    main()
